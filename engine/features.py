def extraer(datos, biblioteca):

    ultimo = datos[0]

    cierre = float(ultimo["close"])
    apertura = float(ultimo["open"])
    maximo = float(ultimo["high"])
    minimo = float(ultimo["low"])
    volumen = float(ultimo["volume"])

    ema9 = biblioteca["ema9"][0]
    ema20 = biblioteca["ema20"][0]

    rango = maximo - minimo

    body_percent = (
        abs(cierre - apertura) / rango
        if rango != 0 else 0
    )

    volumen20 = biblioteca["volumen20"]

    volumen_relativo = (
        volumen / volumen20
        if volumen20 > 0 else 0
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
        "body_percent": body_percent,

        # ==========================
        # VOLUMEN
        # ==========================

        "relative_volume": volumen_relativo,

        # ==========================
        # CAMPOS RESERVADOS V2
        # ==========================

        "sector": None,
        "sector_score": 0,
        "sector_strength": 0,
        "relative_strength": 0,
        "institutional_flow": 0,
        "last_hour_volume": 0,
        "last_hour_strength": 0

    }