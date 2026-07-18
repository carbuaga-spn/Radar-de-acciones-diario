def calcular(actual, historico):

    distancia = 0.0

    # ==========================================
    # TENDENCIA
    # ==========================================

    if actual["above_ema20"] != historico["above_ema20"]:
        distancia += 2.0

    if actual["above_ema9"] != historico["above_ema9"]:
        distancia += 1.5

    distancia += abs(
        actual["ema9_slope"] -
        historico["ema9_slope"]
    )

    distancia += abs(
        actual["ema20_slope"] -
        historico["ema20_slope"]
    )

    if actual["higher_high"] != historico["higher_high"]:
        distancia += 0.5

    if actual["higher_low"] != historico["higher_low"]:
        distancia += 0.5

    # ==========================================
    # MOMENTUM
    # ==========================================

    distancia += abs(
        actual["close_1d_change"] -
        historico["close_1d_change"]
    ) / 10

    distancia += abs(
        actual["close_3d_change"] -
        historico["close_3d_change"]
    ) / 10

    distancia += abs(
        actual["close_5d_change"] -
        historico["close_5d_change"]
    ) / 10

    # ==========================================
    # VOLUMEN
    # ==========================================

    distancia += abs(
        actual["relative_volume"] -
        historico["relative_volume"]
    )

    # ==========================================
    # CUERPO
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
    # MECHAS NORMALIZADAS
    # ==========================================

    distancia += abs(
        actual["upper_wick_percent"] -
        historico["upper_wick_percent"]
    )

    distancia += abs(
        actual["lower_wick_percent"] -
        historico["lower_wick_percent"]
    )

    return distancia