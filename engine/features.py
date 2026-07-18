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

        # =====================================================
        # MERCADO (Market Engine)
        # =====================================================

        "market_strength": 0,
        "market_trend": 0,
        "market_momentum": 0,
        "market_breadth": 0,
        "market_quality": 0,

        # =====================================================
        # SECTOR (Sector Engine)
        # =====================================================

        "sector": None,
        "sector_score": 0,
        "sector_strength": 0,
        "sector_momentum": 0,
        "sector_quality": 0,
        "sector_leader_score": 0,
        "relative_strength": 0,

        # =====================================================
        # FLUJO INSTITUCIONAL
        # =====================================================

        "institutional_flow": 0,
        "last_hour_volume": 0,
        "last_hour_strength": 0,

        # =====================================================
        # CIERRE (Closing Radar)
        # =====================================================

        "closing_quality": 0,
        "momentum_retention": 0,

        # =====================================================
        # FUTURAS DIMENSIONES
        # =====================================================

        "profit_management": 0,
        "risk_quality": 0,
        "decision_score": 0

    }