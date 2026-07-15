from engine.collector import descargar_diario
from libraries.historical_library import construir
from engine.features import extraer
from engine.scorer import calcular_score

TICKERS = [
    "NVDA",
    "AMD",
    "AVGO",
    "MRVL",
    "TSM"
]


def main():

    ranking = []

    print("\n==============================")
    print("AEGIS MVP - Radar Diario")
    print("==============================\n")

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

    ranking.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print("\n==============================")
    print("RANKING AEGIS")
    print("==============================\n")

    for accion in ranking:

        print(
            f'{accion["ticker"]}   '
            f'{accion["score"]} puntos'
        )

        for motivo in accion["motivos"]:
            print("   •", motivo)

        print()


if __name__ == "__main__":
    main()