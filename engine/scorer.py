def calcular_score(c, historico):

    score = 0
    motivos = []

    # ==========================================
    # TENDENCIA
    # ==========================================

    if c["above_ema20"]:
        score += 20
        motivos.append("Sobre EMA20 (+20)")

    if c["above_ema9"]:
        score += 15
        motivos.append("Sobre EMA9 (+15)")

    # ==========================================
    # VOLUMEN
    # ==========================================

    if c["relative_volume"] > 1.5:
        score += 20
        motivos.append("Volumen muy alto (+20)")

    elif c["relative_volume"] > 1.2:
        score += 10
        motivos.append("Volumen alto (+10)")

    # ==========================================
    # CALIDAD DEL CIERRE
    # ==========================================

    if c["closing_quality"] >= 80:
        score += 25
        motivos.append("Cierre de alta calidad (+25)")

    elif c["closing_quality"] >= 60:
        score += 15
        motivos.append("Buen cierre (+15)")

    elif c["closing_quality"] >= 40:
        score += 8
        motivos.append("Cierre aceptable (+8)")

    # ==========================================
    # CONFIANZA HISTÓRICA
    # ==========================================

    confianza = historico["confidence"]

    if confianza >= 80:
        score += 20
        motivos.append("Alta confianza histórica (+20)")

    elif confianza >= 60:
        score += 10
        motivos.append("Buena confianza histórica (+10)")

    elif confianza >= 40:
        score += 5
        motivos.append("Confianza histórica moderada (+5)")

    return {
        "score": score,
        "motivos": motivos
    }