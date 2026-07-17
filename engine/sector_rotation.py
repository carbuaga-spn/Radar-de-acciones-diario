"""
AEGIS - Sector Rotation Engine

Primera versión del detector de rotación sectorial.

Por ahora utiliza una tabla fija de sectores.
Más adelante leerá ETFs (SMH, XLV, XLF...) y datos en tiempo real.
"""


SECTORES = {

    "Semiconductores": [
        "NVDA",
        "AMD",
        "MU",
        "KLAC",
        "AMAT",
        "LRCX",
        "ASML",
        "MRVL",
        "TER",
        "ONTO"
    ],

    "Software": [
        "MSFT",
        "CRM",
        "ORCL",
        "ADBE",
        "NOW",
        "SNOW"
    ],

    "Healthcare": [
        "UNH",
        "ABBV",
        "ABT",
        "LLY",
        "JNJ",
        "ISRG"
    ],

    "Financieras": [
        "JPM",
        "GS",
        "MS",
        "BAC",
        "BLK"
    ],

    "Industriales": [
        "CAT",
        "GE",
        "DE",
        "ETN"
    ]
}


def obtener_sector(ticker):

    ticker = ticker.upper()

    for sector, empresas in SECTORES.items():

        if ticker in empresas:
            return sector

    return "Otros"


def score_sector(sector):

    """
    Versión inicial.

    De momento todos los sectores tienen score 0.

    En la V2 este valor se calculará usando:

    - ETF del sector
    - amplitud
    - fortaleza última hora
    - flujo institucional
    """

    return 0
