from statistics import mean, median


def generar(resultados):

    if not resultados:

        return {
            "total_operaciones": 0,
            "win_rate": 0.0,
            "retorno_medio": 0.0,
            "retorno_mediano": 0.0,
            "mejor_operacion": 0.0,
            "peor_operacion": 0.0,
            "profit_factor": 0.0,
            "expectancy": 0.0,
            "drawdown_medio": 0.0,
            "scores": {}
        }

    retornos = [
        r["retorno_5d"]
        for r in resultados
    ]

    ganadoras = [
        r for r in resultados
        if r["retorno_5d"] > 0
    ]

    perdedoras = [
        r for r in resultados
        if r["retorno_5d"] <= 0
    ]

    win_rate = (
        len(ganadoras)
        / len(resultados)
    ) * 100

    beneficio_total = sum(
        r["retorno_5d"]
        for r in ganadoras
    )

    perdida_total = abs(sum(
        r["retorno_5d"]
        for r in perdedoras
    ))

    if perdida_total > 0:
        profit_factor = (
            beneficio_total
            / perdida_total
        )
    else:
        profit_factor = float("inf")

    expectancy = mean(retornos)

    drawdown_medio = mean(
        r["max_drawdown"]
        for r in resultados
    )

    score_ranges = {}

    for minimo in (50, 60, 70, 80, 90):

        subset = [
            r
            for r in resultados
            if r["score"] >= minimo
        ]

        if subset:

            wr = (
                len([
                    r for r in subset
                    if r["retorno_5d"] > 0
                ])
                / len(subset)
            ) * 100

            avg = mean(
                r["retorno_5d"]
                for r in subset
            )

        else:

            wr = 0.0
            avg = 0.0

        score_ranges[minimo] = {

            "operaciones": len(subset),

            "win_rate": wr,

            "retorno_medio": avg

        }

    return {

        "total_operaciones": len(resultados),

        "win_rate": win_rate,

        "retorno_medio": mean(retornos),

        "retorno_mediano": median(retornos),

        "mejor_operacion": max(retornos),

        "peor_operacion": min(retornos),

        "profit_factor": profit_factor,

        "expectancy": expectancy,

        "drawdown_medio": drawdown_medio,

        "scores": score_ranges

    }