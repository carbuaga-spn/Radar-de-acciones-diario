from engine.collector import descargar_diario
from libraries.historical_library import construir
from engine.features import extraer
from engine.historical_comparison import comparar
from engine.scorer import calcular_score
from engine.ranking import seleccionar_mejores
from radars.close_radar import mostrar

from config.universe import cargar_universo
from config.radars import cargar_radar


def main():

    ranking = []

    radar = cargar_radar("close")

    tickers = cargar_universo()

    print()
    print("===================================")
    print("AEGIS V1")
    print("Radar Cierre")
    print("===================================")
    print()

    for ticker in tickers:

        print("Analizando", ticker)

        try:

            datos = descargar_diario(ticker)

            biblioteca = construir(datos)

            caracteristicas = extraer(datos, biblioteca)

            historico = comparar(caracteristicas)

            resultado = calcular_score(caracteristicas)

            ranking.append({

                "ticker": ticker,

                "score": resultado["score"],

                "motivos": resultado["motivos"],

                "historico": historico

            })

        except Exception as e:

            print("ERROR", ticker)

            print(e)

    ranking = seleccionar_mejores(

        ranking,

        minimo=radar["min_score"],

        limite=radar["top"]

    )

    mostrar(ranking)


if __name__ == "__main__":

    main()