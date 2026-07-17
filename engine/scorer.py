def calcular_score(c):

    score = 0
    motivos = []

    # =====================================
    # TÉCNICO
    # =====================================

    tecnico = 0

    if c["above_ema20"]:
        tecnico += 20

    if c["above_ema9"]:
        tecnico += 15

    if c["green_day"]:
        tecnico += 10

    if c["body_percent"] > 0.60:
        tecnico += 15

    if c["relative_volume"] > 1.5:
        tecnico += 20

    elif c["relative_volume"] > 1.2:
        tecnico += 10

    score += tecnico

    motivos.append(f"Técnico: {tecnico}")

    # =====================================
    # SECTOR
    # =====================================

    sector = c.get("sector_score", 0)

    score += sector

    if sector > 0:
        motivos.append(f"Sector: {sector}")

    # =====================================
    # FLUJO INSTITUCIONAL
    # =====================================

    flujo = c.get("institutional_flow", 0)

    flujo_aplicado = round(flujo * 0.40)

    score += flujo_aplicado

    if flujo_aplicado > 0:
        motivos.append(f"Flujo: {flujo_aplicado}")

    # =====================================
    # TOTAL
    # =====================================

    return {

        "score": round(score),

        "motivos": motivos

    }