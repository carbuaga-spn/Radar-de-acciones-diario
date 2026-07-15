from engine.collector import descargar_diario
from storage.save_json import guardar_json

TICKERS = [
    "NVDA",
    "AMD",
    "AVGO",
    "MRVL",
    "TSM"
]


def main():

    print("======================================")
    print("AEGIS - Biblioteca Histórica")
    print("======================================")

    for ticker in TICKERS:

        print(f"\nDescargando {ticker}...")

        try:

            datos = descargar_diario(ticker)

            guardar_json(ticker, datos)

            print(f"OK - {ticker}: {len(datos)} sesiones guardadas")

        except Exception as e:

            print(f"ERROR - {ticker}")
            print(e)

    print("\nProceso terminado.")


if __name__ == "__main__":
    main()