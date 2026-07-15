def seleccionar_mejores(ranking, minimo=40, limite=10):

    candidatos = []

    for accion in ranking:

        if accion["score"] >= minimo:
            candidatos.append(accion)

    candidatos.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return candidatos[:limite]
