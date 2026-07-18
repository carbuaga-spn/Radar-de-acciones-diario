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
    # HISTÓRICO
    # (Preparado para futuras versiones)
    # ==========================================

    # Próximamente:
    # score += ...
    # motivos.append(...)

    return {
        "score": score,
        "motivos": motivos
    }