def comparar(c):

    confidence = 0
    matches = 0

    # ==========================================
    # CALIDAD DEL PATRÓN ACTUAL
    # ==========================================

    if c["above_ema20"]:
        confidence += 20
        matches += 1

    if c["above_ema9"]:
        confidence += 15
        matches += 1

    if c["relative_volume"] > 1.2:
        confidence += 20
        matches += 1

    if c["closing_quality"] >= 80:
        confidence += 25
        matches += 1

    if c["range_position_20"] >= 0.80:
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