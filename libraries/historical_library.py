from engine.indicators import ema, volumen_medio


def construir(datos):

    ema9 = ema(datos, 9)

    ema20 = ema(datos, 20)

    volumen20 = volumen_medio(datos)

    ultimas20 = datos[:20]

    high20 = max(float(vela["high"]) for vela in ultimas20)

    low20 = min(float(vela["low"]) for vela in ultimas20)

    return {

        "ema9": ema9,

        "ema20": ema20,

        "volumen20": volumen20,

        "high20": high20,

        "low20": low20

    }