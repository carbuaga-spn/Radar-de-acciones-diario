from engine.historical_library import construir
from engine.features import extraer
from engine.historical_comparison import comparar
from engine.scorer import calcular as calcular_score


def ejecutar(datos):

    biblioteca = construir(datos)

    resultados = []

    for i in range(30, len(datos) - 10):

        caracteristicas = extraer(
            datos,
            biblioteca,
            i
        )

        historico = comparar(
            caracteristicas,
            datos[i:]
        )

        score = calcular_score(
            caracteristicas,
            historico
        )

        entrada = float(datos[i]["close"])

        salida_5d = float(datos[i - 5]["close"])

        retorno_5d = (
            (salida_5d - entrada)
            / entrada
        ) * 100

        resultados.append({

            "indice": i,

            "fecha": datos[i]["date"],

            "ticker": datos[i].get(
                "symbol",
                ""
            ),

            "score": score,

            "retorno_5d": retorno_5d,

            "win_rate": historico["win_rate"],

            "avg_return_5d": historico["avg_return_5d"],

            "avg_return_10d": historico["avg_return_10d"],

            "max_drawdown": historico["max_drawdown"],

            "matches": historico["matches"]

        })

    return resultados