"""
AEGIS - Sector Rotation Engine
Versión 2
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

    # Agrupar acciones por sector
    for accion in acciones:

        sector = accion["sector"]

        sectores.setdefault(sector, []).append(accion)

    scores = {}

    for sector, lista in sectores.items():

        total = 0

        for accion in lista:

            c = accion["caracteristicas"]

            if c["above_ema20"]:
                total += 2

            if c["above_ema9"]:
                total += 1

            if c["green_day"]:
                total += 1

            if c["relative_volume"] > 1.2:
                total += 2

            if c["body_percent"] > 0.60:
                total += 1

        promedio = total / len(lista)

        scores[sector] = round(promedio)

    return scores