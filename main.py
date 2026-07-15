
        from engine.collector import descargar_diario
from libraries.historical_library import construir
from engine.features import extraer
from engine.scorer import calcular_score
from radars.close_radar import mostrar

TICKERS = [
    "NVDA",
    "AMD",
    "AVGO",
    "MRVL",
    "TSM"
]


def main():

    ranking = []

    print("\n================================")
    print("AEGIS MVP")
    print("================================\n")

    for ticker in TICKERS:

        print(f"Analizando {ticker}")

        try:

            datos = descargar_diario(ticker)

            biblioteca = construir(datos)

            caracteristicas = extraer(datos, biblioteca)

            resultado = calcular_score(caracteristicas)

            ranking.append({

                "ticker": ticker,

                "score": resultado["score"],

                "motivos": resultado["motivos"]

            })

        except Exception as e:

            print(f"ERROR en {ticker}")

            print(e)

    mostrar(ranking)


if __name__ == "__main__":
    main()