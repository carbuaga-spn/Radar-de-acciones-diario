def ema(datos, periodo):

    alpha = 2 / (periodo + 1)

    cierres = [float(d["close"]) for d in reversed(datos)]

    ema_actual = cierres[0]

    resultado = []

    for precio in cierres:

        ema_actual = alpha * precio + (1 - alpha) * ema_actual

        resultado.append(ema_actual)

    return list(reversed(resultado))


def volumen_medio(datos, sesiones=20):

    volumenes = [
        float(d["volume"])
        for d in datos[:sesiones]
    ]

    return sum(volumenes) / len(volumenes)
