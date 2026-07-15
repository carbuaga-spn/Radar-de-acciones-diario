from engine.collector import descargar_diario
from libraries.historical_library import construir
from engine.features import extraer

TICKERS = [
    "NVDA",
    "AMD",
    "AVGO",
    "MRVL",
    "TSM"
]


def main():

    print("\n==========================")
    print("AEGIS - Motor de Análisis")
    print("==========================\n")

    for ticker in TICKERS:

        print(f"Analizando {ticker}")

        try:

            datos = descargar_diario(ticker)

            biblioteca = construir(datos)

            caracteristicas = extraer(datos, biblioteca)

            print(caracteristicas)

            print("----------------------------------")

        except Exception as e:

            print(f"ERROR en {ticker}")

            print(e)

            print("----------------------------------")


if __name__ == "__main__":
    main()