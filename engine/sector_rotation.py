"""
AEGIS - Sector Rotation Engine
Versión 3
"""


SECTORES = {

    "Semiconductores": [
        "NVDA", "AMD", "MU", "KLAC",
        "AMAT", "LRCX", "ASML",
        "MRVL", "TER", "ONTO"
    ],

    "Software": [
        "MSFT", "CRM", "ORCL",
        "ADBE", "NOW", "SNOW"
    ],

    "Healthcare": [
        "UNH", "ABBV", "ABT",
        "LLY", "JNJ", "ISRG"
    ],

    "Financieras": [
        "JPM", "GS", "MS",
        "BAC", "BLK"
    ],

    "Industriales": [
        "CAT", "GE", "DE", "ETN"
    ]
}


def obtener_sector(ticker):

    ticker = ticker.upper()

    for sector, empresas in SECTORES.items():

        if ticker in empresas:
            return sector

    return "Otros"


def calcular_scores_sector(acciones):

    sectores = {}

    for accion in acciones:

        sector = accion["sector"]

        sectores.setdefault(sector, []).append(
            accion["caracteristicas"]
        )

    resultado = {}

    for sector, lista in sectores.items():

        total = len(lista)

        sobre_ema20 = 0
        sobre_ema9 = 0
        verdes = 0
        volumen = 0
        cuerpos = 0

        for c in lista:

            if c["above_ema20"]:
                sobre_ema20 += 1

            if c["above_ema9"]:
                sobre_ema9 += 1

            if c["green_day"]:
                verdes += 1

            if c["relative_volume"] > 1.2:
                volumen += 1

            if c["body_percent"] > 0.60:
                cuerpos += 1

        score = (
            sobre_ema20 * 2 +
            sobre_ema9 +
            verdes +
            volumen * 2 +
            cuerpos
        ) / total

        resultado[sector] = {

            "score": round(score),

            "acciones": total,

            "sobre_ema20": sobre_ema20,

            "sobre_ema9": sobre_ema9,

            "verdes": verdes,

            "volumen": volumen,

            "cuerpos": cuerpos

        }

    return resultado