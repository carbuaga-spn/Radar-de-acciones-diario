def calcular(coincidencias):

    if not coincidencias:

        return {

            "matches": 0,

            "win_rate": 0.0,

            "avg_return_5d": 0.0,

            "avg_return_10d": 0.0,

            "max_drawdown": 0.0,

            "confidence": 0.0

        }

    matches = len(coincidencias)

    positivos = sum(
        1
        for c in coincidencias
        if c["retorno_5d"] > 0
    )

    win_rate = (
        positivos / matches
    ) * 100

    avg_return_5d = sum(
        c["retorno_5d"]
        for c in coincidencias
    ) / matches

    avg_return_10d = sum(
        c["retorno_10d"]
        for c in coincidencias
    ) / matches

    max_drawdown = min(
        c["drawdown"]
        for c in coincidencias
    )

    confidence = min(
        100,
        (
            win_rate * 0.5 +
            max(0, avg_return_5d) * 5 +
            matches * 0.5
        )
    )

    return {

        "matches": matches,

        "win_rate": win_rate,

        "avg_return_5d": avg_return_5d,

        "avg_return_10d": avg_return_10d,

        "max_drawdown": max_drawdown,

        "confidence": confidence

    }