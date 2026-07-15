from engine.collector import descargar_diario
from libraries.historical_library import construir

TICKERS = [
    "NVDA",
    "AMD",
    "AVGO",
    "MRVL",
    "TSM"
]


def main():

    print("\nAEGIS\n")

    for ticker in TICKERS:

        print(f"\nAnalizando {ticker}")

        datos = descargar_diario(ticker)

        biblioteca = construir(datos)

        print("EMA9:", round(biblioteca["ema9"][0],2))
        print("EMA20:", round(biblioteca["ema20"][0],2))
        print("Volumen20:", round(biblioteca["volumen20"]))

if __name__ == "__main__":
    main()