from engine.collector import descargar_diario
from engine.historical_library import construir
from engine.features import extraer
from engine.historical_comparison import comparar
from engine.scorer import calcular_score
from engine.backtest_report import generar

from config.universe import cargar_universo


def main():

    universo = cargar_universo()

    resultados = []

    print()
    print("===================================")
    print("AEGIS BACKTEST")
    print("===================================")
    print()

    for ticker in universo:

        print("Backtesting", ticker)

        try:

            datos = descargar_diario(ticker)

            biblioteca = construir(datos)

            for i in range(30, len(datos) - 10):

                caracteristicas = extraer(
                    datos,
                    biblioteca,
                    i
                )

                historico = comparar(
                    caracteristicas,
                    datos,
                    indice_actual=i
                )

                score = calcular_score(
                    caracteristicas,
                    historico
                )

                entrada = float(
                    datos[i]["close"]
                )

                salida = float(
                    datos[i - 5]["close"]
                )

                retorno = (
                    (salida - entrada)
                    / entrada
                ) * 100

                resultados.append({

                    "ticker": ticker,

                    "fecha": datos[i]["date"],

                    "score": score["score"],

                    "retorno_5d": retorno,

                    "max_drawdown": historico["max_drawdown"]

                })

        except Exception as e:

            print("ERROR", ticker)

            print(e)

    reporte = generar(resultados)

    print()
    print("============== RESUMEN ==============")
    print()

    print("Operaciones :", reporte["total_operaciones"])

    print("Win Rate    : {:.2f}%".format(
        reporte["win_rate"]
    ))

    print("Retorno Medio: {:.2f}%".format(
        reporte["retorno_medio"]
    ))

    print("Profit Factor:", round(
        reporte["profit_factor"], 2
    ))

    print("Expectancy :", round(
        reporte["expectancy"], 2
    ))

    print("Drawdown Medio:", round(
        reporte["drawdown_medio"], 2
    ))

    print()

    print("========== POR SCORE ==========")

    for score, datos in reporte["scores"].items():

        print()

        print("Score >=", score)

        print("Operaciones :", datos["operaciones"])

        print("Win Rate    : {:.2f}%".format(
            datos["win_rate"]
        ))

        print("Retorno Medio: {:.2f}%".format(
            datos["retorno_medio"]
        ))


if __name__ == "__main__":

    main()