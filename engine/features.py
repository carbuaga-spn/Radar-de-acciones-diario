def extraer(datos, biblioteca, indice=0):

    vela = datos[indice]

    cierre = float(vela["close"])
    apertura = float(vela["open"])
    maximo = float(vela["high"])
    minimo = float(vela["low"])
    volumen = float(vela["volume"])

    ema9 = biblioteca["ema9"][indice]
    ema20 = biblioteca["ema20"][indice]

    rango = maximo - minimo

    body = abs(cierre - apertura)

    body_percent = (
        body / rango
        if rango > 0 else 0
    )

    volumen20 = biblioteca["volumen20"]

    relative_volume = (
        volumen / volumen20
        if volumen20 > 0 else 0
    )

    upper_wick = (
        maximo - max(cierre, apertura)
    )

    lower_wick = (
        min(cierre, apertura) - minimo
    )

    close_position = (
        (cierre - minimo) / rango
        if rango > 0 else 0
    )

    return {

        # ==========================
        # DATOS DEL DÍA
        # ==========================

        "close": cierre,
        "open": apertura,
        "high": maximo,
        "low": minimo,
        "volume": volumen,

        # ==========================
        # MEDIAS
        # ==========================

        "ema9": ema9,
        "ema20": ema20,
        "volumen20": volumen20,

        # ==========================
        # TENDENCIA
        # ==========================

        "above_ema9": cierre > ema9,
        "above_ema20": cierre > ema20,

        # ==========================
        # VELA
        # ==========================

        "green_day": cierre > apertura,

        "range": rango,

        "body": body,

        "body_percent": body_percent,

        "upper_wick": upper_wick,

        "lower_wick": lower_wick,

        "close_position": close_position,

        # ==========================
        # VOLUMEN
        # ==========================

        "relative_volume": relative_volume,

        # ==========================
        # CAMPOS RESERVADOS V2
        # ==========================

        "sector": None,

        "sector_score": 0,

        "sector_strength": 0,

        "relative_strength": 0,

        "institutional_flow": 0,

        "last_hour_volume": 0,

        "last_hour_strength": 0,

        # ==========================
        # CAMPOS FUTUROS
        # ==========================

        "market_strength": 0,

        "news_score": 0,

        "breakout_score": 0,

        "momentum_score": 0

    }