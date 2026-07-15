from engine.indicators import ema, volumen_medio


def construir(datos):

    ema9 = ema(datos, 9)

    ema20 = ema(datos, 20)

    return {

        "ema9": ema9,

        "ema20": ema20,

        "volumen20": volumen_medio(datos)

    }
