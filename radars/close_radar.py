def mostrar(ranking):

    ranking.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print()
    print("====================================================")
    print("              AEGIS - RADAR CIERRE")
    print("====================================================")
    print()

    print(f"Acciones analizadas: {len(ranking)}")
    print()

    for i, accion in enumerate(ranking, start=1):

        if accion["score"] >= 70:
            confianza = "ALTA"

        elif accion["score"] >= 40:
            confianza = "MEDIA"

        else:
            confianza = "BAJA"

        print(f"{i}. {accion['ticker']}")
        print(f"   Score: {accion['score']}")
        print(f"   Confianza: {confianza}")

        if accion["motivos"]:

            print("   Motivos:")

            for motivo in accion["motivos"]:
                print(f"      • {motivo}")

        else:

            print("   Motivos: Ninguno")

        print()

    mejor = ranking[0]

    if mejor["score"] >= 70:
        confianza = "ALTA"

    elif mejor["score"] >= 40:
        confianza = "MEDIA"

    else:
        confianza = "BAJA"

    print("====================================================")
    print("MEJOR CANDIDATA DEL DÍA")
    print("====================================================")
    print()

    print(mejor["ticker"])
    print(f"Score: {mejor['score']}")
    print(f"Confianza: {confianza}")

    if mejor["motivos"]:
        print()
        print("Razones principales:")

        for motivo in mejor["motivos"]:
            print(f" - {motivo}")

    print()
    print("====================================================")