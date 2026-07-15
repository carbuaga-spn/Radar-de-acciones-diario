def extraer(datos, biblioteca):

    ultimo = datos[0]

    cierre = float(ultimo["close"])
    apertura = float(ultimo["open"])
    maximo = float(ultimo["high"])
    minimo = float(ultimo["low"])
    volumen = float(ultimo["volume"])

    ema9 = biblioteca["ema9"][0]
    ema20 = biblioteca["ema20"][0]

    return {

        "close": cierre,
        "open": apertura,
        "high": maximo,
        "low": minimo,
        "volume": volumen,

        "ema9": ema9,
        "ema20": ema20,

        "above_ema9": cierre > ema9,
        "above_ema20": cierre > ema20,

        "green_day": cierre > apertura,

        "body_percent":
            abs(cierre-apertura)/(maximo-minimo)
            if maximo != minimo else 0

    }