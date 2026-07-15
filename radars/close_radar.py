    from scorer import score

def radar(lista):

    sesiones = [score(s) for s in lista]

    sesiones.sort(
        key=lambda x: x.action_score,
        reverse=True
    )

    return sesiones
