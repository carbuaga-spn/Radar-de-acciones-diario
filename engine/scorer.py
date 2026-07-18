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
    # CALIDAD DEL PATRÓN
    # ==========================================

    if c["close_position"] >= 0.80:
        score += 15
        motivos.append("Cierre cerca del máximo (+15)")

    elif c["close_position"] >= 0.60:
        score += 8
        motivos.append("Buen cierre (+8)")

    if c["body_percent"] >= 0.60:
        score += 10
        motivos.append("Cuerpo sólido (+10)")

    # ==========================================
    # RESULTADO HISTÓRICO
    # ==========================================

    if historico["win_rate"] >= 70:
        score += 20
        motivos.append("Win rate histórico alto (+20)")

    elif historico["win_rate"] >= 60:
        score += 10
        motivos.append("Win rate histórico positivo (+10)")

    if historico["avg_return_5d"] > 3:
        score += 15
        motivos.append("Rentabilidad media 5d elevada (+15)")

    elif historico["avg_return_5d"] > 1:
        score += 8
        motivos.append("Rentabilidad media 5d positiva (+8)")

    numero_coincidencias = len(historico["coincidencias"])

    if numero_coincidencias >= 30:
        score += 10
        motivos.append("Muchos patrones similares (+10)")

    elif numero_coincidencias >= 10:
        score += 5
        motivos.append("Patrones suficientes (+5)")

    score = min(score, 100)

    return {
        "score": score,
        "motivos": motivos
    }