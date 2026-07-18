from engine.features import extraer
from engine.historical_library import construir
from engine.pattern_distance import calcular


DISTANCIA_MAXIMA = 2.5


def comparar(caracteristicas, datos):

    confidence = 0
    matches = 0

    biblioteca = construir(datos)

    coincidencias = []

    for i in range(20, len(datos) - 10):

        patron = extraer(
            datos,
            biblioteca,
            i
        )

        distancia = calcular(
            caracteristicas,
            patron
        )

        if distancia > DISTANCIA_MAXIMA:
            continue

        entrada = float(datos[i]["close"])

        salida_5d = float(datos[i - 5]["close"])

        salida_10d = float(datos[i - 10]["close"])

        retorno_5d = (
            (salida_5d - entrada) / entrada
        ) * 100

        retorno_10d = (
            (salida_10d - entrada) / entrada
        ) * 100

        coincidencias.append({

            "indice": i,

            "distancia": distancia,

            "entrada": entrada,

            "retorno_5d": retorno_5d,

            "retorno_10d": retorno_10d

        })

    coincidencias.sort(
        key=lambda x: x["distancia"]
    )

    mejores = coincidencias

    if mejores:

        positivos = sum(
            1 for c in mejores
            if c["retorno_5d"] > 0
        )

       