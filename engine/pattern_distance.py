def calcular(actual, historico):

    distancia = 0.0

    # ==========================================
    # TENDENCIA
    # ==========================================

    if actual["above_ema20"] != historico["above_ema20"]:
        distancia += 2.0

    if actual["above_ema9"] != historico["above_ema9"]:
        distancia += 1.5

    # ==========================================
    # VOLUMEN
    # ==========================================

    distancia += abs(
        actual["relative_volume"] -
        historico["relative_volume"]
    )

    # ==========================================
    # CUERPO DE LA VELA
    # ==========================================

    distancia += abs(
        actual["body_percent"] -
        historico["body_percent"]
    )

    # ==========================================
    # POSICIÓN DEL CIERRE
    # ==========================================

    distancia += abs(
        actual["close_position"] -
        historico["close_position"]
    )

    # ==========================================
    # DIRECCIÓN DE LA VELA
    # ==========================================

    if actual["green_day"] != historico["green_day"]:
        distancia += 0.5

    # ==========================================
    # MECHAS
    # ==========================================

    distancia += abs(
        actual["upper_wick"] -
        historico["upper_wick"]
    )

    distancia += abs(
        actual["lower_wick"] -
        historico["lower_wick"]
    )

    return distancia