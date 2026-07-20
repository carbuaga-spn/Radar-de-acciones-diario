from engine.features import extraer
from engine.historical_library import construir
from engine.pattern_distance import calcular
from engine.pattern_statistics import calcular as calcular_estadisticas


MAX_COINCIDENCIAS = 30


def comparar(caracteristicas, datos, indice_actual=None):

    biblioteca = construir(datos)

    coincidencias = []

    if indice_actual is None:
        indice_actual = len(datos)

    limite_superior = min(
        indice_actual - 10,
        len(datos) - 10
    )

    for i in range(20, limite_superior):

        patron = extraer(
            datos,
            biblioteca,
            i
        )

        distancia = calcular(
            caracteristicas,
            patron
        )

        entrada = float(datos[i]["close"])

        salida_5d = float(datos[i - 5]["close"])

        salida_10d = float(datos[i - 10]["close"])

        retorno_5d = (
            (salida_5d - entrada)
            / entrada
        ) * 100

        retorno_10d = (
            (salida_10d - entrada)
            / entrada
        ) * 100

        minimo = entrada

        for j in range(i - 10, i + 1):

            if j < 0:
                continue

            minimo = min(
                minimo,
                float(datos[j]["low"])
            )

        drawdown = (
            (minimo - entrada)
            / entrada
        ) * 100

        coincidencias.append({

            "indice": i,

            "distancia": distancia,

            "entrada": entrada,

            "retorno_5d": retorno_5d,

            "retorno_10d": retorno_10d,

            "drawdown": drawdown

        })

    coincidencias.sort(
        key=lambda x: x["distancia"]
    )

    mejores = coincidencias[:MAX_COINCIDENCIAS]

    estadisticas = calcular_estadisticas(
        mejores
    )

    return {

        **estadisticas,

        "coincidencias": mejores

    }