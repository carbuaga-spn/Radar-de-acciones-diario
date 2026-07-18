def score_market(features):
    return 0, []


def score_sector(features):
    sector = features.get("sector_score", 0)

    motivos = []

    if sector > 0:
        motivos.append(f"Sector: {sector}")

    return sector, motivos


def score_sector_synchronization(features):
    return 0, []


def score_institutional_flow(features):
    flujo = features.get("institutional_flow", 0)

    score = round(flujo * 0.40)

    motivos = []

    if score > 0:
        motivos.append(f"Flujo: {score}")

    return score, motivos


def score_sector_leader(features):
    return 0, []


def score_closing_quality(features):

    score = 0

    motivos = []

    if features["above_ema20"]:
        score += 20

    if features["above_ema9"]:
        score += 15

    if features["green_day"]:
        score += 10

    if features["body_percent"] > 0.60:
        score += 15

    if features["relative_volume"] > 1.5:
        score += 20

    elif features["relative_volume"] > 1.2:
        score += 10

    motivos.append(f"Técnico: {score}")

    return score, motivos


def score_momentum_retention(features):
    return 0, []