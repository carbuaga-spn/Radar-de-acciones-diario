def calcular(actual, historico):

    distancia = 0

    if actual["above_ema20"] != historico["above_ema20"]:
        distancia += 1

    if actual["above_ema9"] != historico["above_ema9"]:
        distancia += 1

    distancia += abs(
        actual["body_percent"] -
        historico["body_percent"]
    )

    distancia += abs(
        actual["relative_volume"] -
        historico["relative_volume"]
    )

    distancia += abs(
        actual["close_position"] -
        historico["close_position"]
    )

    return distancia