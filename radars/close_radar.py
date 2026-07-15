def mostrar(ranking):

    print()
    print("========================================")
    print("        RADAR CIERRE AEGIS")
    print("========================================")
    print()

    ranking.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    for i, accion in enumerate(ranking, start=1):

        print(f"{i}. {accion['ticker']}")
        print(f"Score: {accion['score']}")

        print("Motivos:")

        for motivo in accion["motivos"]:
            print("   •", motivo)

        print("----------------------------------------")