def extraer(datos, biblioteca, indice=0):

    vela = datos[indice]

    cierre = float(vela["close"])
    apertura = float(vela["open"])
    maximo = float(vela["high"])
    minimo = float(vela["low"])
    volumen = float(vela["volume"])

    ema9 = biblioteca["ema9"][indice]
    ema20 = biblioteca["ema20"][indice]

    volumen20 = biblioteca["volumen20"][indice]

    rango = maximo - minimo

    body = abs(cierre - apertura)

    body_percent = (
        body / rango
        if rango > 0 else 0
    )

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

    upper_wick_percent = (
        upper_wick / rango
        if rango > 0 else 0
    )

    lower_wick_percent = (
        lower_wick / rango
        if rango > 0 else 0
    )

    close_position = (
        (cierre - minimo) / rango
        if rango > 0 else 0
    )

    # ==========================================
    # CONTEXTO DEL MERCADO
    # ==========================================

    close_1d_change = 0
    close_3d_change = 0
    close_5d_change = 0

    ema9_slope = 0
    ema20_slope = 0

    higher_high = False
    higher_low = False

    if indice + 1 < len(datos):

        cierre_1 = float(datos[indice + 1]["close"])

        close_1d_change = (
            (cierre - cierre_1) / cierre_1
        ) * 100

        higher_high = (
            maximo >
            float(datos[indice + 1]["high"])
        )

        higher_low = (
            minimo >
            float(datos[indice + 1]["low"])
        )

        ema9_slope = (
            ema9 -
            biblioteca["ema9"][indice + 1]
        )

        ema20_slope = (
            ema20 -
            biblioteca["ema20"][indice + 1]
        )

    if indice + 3 < len(datos):

        cierre_3 = float(datos[indice + 3]["close"])

        close_3d_change = (
            (cierre - cierre_3) / cierre_3
        ) * 100

    if indice + 5 < len(datos):

        cierre_5 = float(datos[indice + 5]["close"])

        close_5d_change = (
            (cierre - cierre_5) / cierre_5
        ) * 100

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

        "ema9_slope": ema9_slope,
        "ema20_slope": ema20_slope,

        "higher_high": higher_high,
        "higher_low": higher_low,

        # ==========================
        # MOMENTUM
        # ==========================

        "close_1d_change": close_1d_change,
        "close_3d_change": close_3d_change,
        "close_5d_change": close_5d_change,

        # ==========================
        # VELA
        # ==========================

        "green_day": cierre > apertura,

        "range": rango,

        "body": body,

        "body_percent": body_percent,

        "upper_wick": upper_wick,

        "lower_wick": lower_wick,

        "upper_wick_percent": upper_wick_percent,

        "lower_wick_percent": lower_wick_percent,

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