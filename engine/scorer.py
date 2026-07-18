from engine.score_dimensions import (
    score_market,
    score_sector,
    score_sector_synchronization,
    score_institutional_flow,
    score_sector_leader,
    score_closing_quality,
    score_momentum_retention,
)


def calcular_score(features):

    score_total = 0
    motivos = []

    dimensiones = [

        score_market,

        score_sector,

        score_sector_synchronization,

        score_institutional_flow,

        score_sector_leader,

        score_closing_quality,

        score_momentum_retention,

    ]

    for dimension in dimensiones:

        puntos, razones = dimension(features)

        score_total += puntos

        motivos.extend(razones)

    return {

        "score": round(score_total),

        "motivos": motivos

    }