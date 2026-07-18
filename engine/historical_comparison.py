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

        # ==========================================
        # DRAWDOWN MÁXIMO EN LOS 10 DÍAS SIGUIENTES
        # ==========================================

        minimo = entrada

        for j in range(i - 10, i + 1):

            if j < 0:
                continue

            minimo = min(
                minimo,
                float(datos[j]["low"])
            )

        max_drawdown = (
            (minimo - entrada) / entrada
        ) * 100

        coincidencias.append({

            "indice": i,

            "distancia": distancia,

            "entrada": entrada,

            "retorno_5d": retorno_5d,

            "retorno_10d": retorno_10d,

            "drawdown": max_drawdown

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

        win_rate = positivos / len(mejores) * 100

        avg_return_5d = sum(
            c["retorno_5d"] for c in mejores
        ) / len(mejores)

        avg_return_10d = sum(
            c["retorno_10d"] for c in mejores
        ) / len(mejores)

        max_drawdown = min(
            c["drawdown"] for c in mejores
        )

    else:

        win_rate = 0.0
        avg_return_5d = 0.0
        avg_return_10d = 0.0
        max_drawdown = 0.0

    if caracteristicas["above_ema20"]:
        confidence += 20
        matches += 1

    if caracteristicas["above_ema9"]:
        confidence += 15
        matches += 1

    if caracteristicas["relative_volume"] > 1.2:
        confidence += 20
        matches += 1

    confidence = min(confidence, 100)

    return {

        "matches": matches,

        "win_rate": win_rate,

        "avg_return_5d": avg_return_5d,

        "avg_return_10d": avg_return_10d,

        "max_drawdown": max_drawdown,

        "confidence": confidence,

        "coincidencias": mejores

    }