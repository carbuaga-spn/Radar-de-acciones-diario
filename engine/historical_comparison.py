def comparar(caracteristicas, datos):

    confidence = 0
    matches = 0

    # =====================================================
    # PREPARADO PARA COMPARACIÓN HISTÓRICA
    # =====================================================

    for i in range(20, len(datos) - 10):

        # Aquí construiremos en próximas versiones
        # el patrón histórico de la sesión i

        pass

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

    if caracteristicas["closing_quality"] >= 80:
        confidence += 25
        matches += 1

    if caracteristicas["range_position_20"] >= 0.80:
        confidence += 20
        matches += 1

    confidence = min(confidence, 100)

    return {

        "matches": matches,

        "win_rate": 0.0,

        "avg_return_5d": 0.0,

        "avg_return_10d": 0.0,

        "max_drawdown": 0.0,

        "confidence": confidence

    }