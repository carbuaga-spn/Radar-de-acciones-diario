def calcular_score(c):

    score = 0
    motivos = []

    if c["above_ema20"]:
        score += 20
        motivos.append("Sobre EMA20 (+20)")

    if c["above_ema9"]:
        score += 15
        motivos.append("Sobre EMA9 (+15)")

    if c["green_day"]:
        score += 10
        motivos.append("Vela verde (+10)")

    if c["body_percent"] > 0.60:
        score += 15
        motivos.append("Cuerpo fuerte (+15)")

    volumen_relativo = c["volume"] / c["volumen20"]

    if volumen_relativo > 1.5:
        score += 20
        motivos.append("Volumen muy alto (+20)")

    elif volumen_relativo > 1.2:
        score += 10
        motivos.append("Volumen alto (+10)")

    return {
        "score": score,
        "motivos": motivos
    }