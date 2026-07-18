from engine.features import extraer
from engine.historical_library import construir
from engine.pattern_distance import calcular


def comparar(caracteristicas, datos):

    confidence = 0
    matches = 0

    # =====================================================
    # COMPARACIÓN HISTÓRICA
    # =====================================================

    coincidencias = []

    for i in range(20, len(datos) - 10):

        datos_historicos = datos[i:]

        biblioteca = construir(datos_historicos)

        patron = extraer(
            datos_historicos,
            biblioteca
        )

        distancia = calcular(
            caracteristicas,
            patron
        )

        coincidencias.append({

            "indice": i,

            "distancia": distancia

        })

    coincidencias.sort(
        key=lambda x: x["distancia"]
    )

    # =====================================================
    # EVALUACIÓN TEMPORAL
    # =====================================================

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

        "win_rate": 0.0,

        "avg_return_5d": 0.0,

        "avg_return_10d": 0.0,

        "max_drawdown": 0.0,

        "confidence": confidence,

        "coincidencias": coincidencias[:10]

    }