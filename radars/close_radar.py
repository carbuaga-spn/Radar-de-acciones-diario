def mostrar(ranking):

    print()
    print("====================================================")
    print("          AEGIS - RADAR CIERRE")
    print("====================================================")
    print()

    if len(ranking) == 0:

        print("No se han encontrado oportunidades hoy.")
        return

    print(f"Candidatas encontradas: {len(ranking)}")
    print()

    for i, accion in enumerate(ranking, start=1):

        if accion["score"] >= 70:
            confianza = "ALTA"

        elif accion["score"] >= 50:
            confianza = "MEDIA"

        else:
            confianza = "BAJA"

        print(f"{i}. {accion['ticker']}")
        print(f"Score: {accion['score']}")
        print(f"Confianza: {confianza}")

        for motivo in accion["motivos"]:
            print(" -", motivo)

        print()

    mejor = ranking[0]

    print("====================================================")
    print("MEJOR OPORTUNIDAD DEL DÍA")
    print("====================================================")
    print()

    print(mejor["ticker"])
    print(f"Score: {mejor['score']}")