from engine.collector import descargar_diario
from libraries.historical_library import construir
from engine.features import extraer
from engine.scorer import calcular_score
from engine.ranking import seleccionar_mejores
from engine.sector_rotation import (
    obtener_sector,
    calcular_scores_sector
)


def ejecutar_radar(tickers, radar):

    # =====================================
    # FASE 1
    # Analizar acciones
    # =====================================

    acciones = []

    for ticker in tickers:

        print("Analizando", ticker)

        try:

            datos = descargar_diario(ticker)

            biblioteca = construir(datos)

            caracteristicas = extraer(datos, biblioteca)

            sector = obtener_sector(ticker)

            caracteristicas["sector"] = sector

            acciones.append({

                "ticker": ticker,

                "sector": sector,

                "caracteristicas": caracteristicas

            })

        except Exception as e:

            print("ERROR", ticker)
            print(e)

    # =====================================
    # FASE 2
    # Analizar sectores
    # =====================================

    scores_sector = calcular_scores_sector(acciones)

    # =====================================
    # FASE 3
    # Score final
    # =====================================

    ranking = []

    for accion in acciones:

        caracteristicas = accion["caracteristicas"]

        info_sector = scores_sector.get(

            accion["sector"],

            {"score": 0}

        )

        caracteristicas["sector_score"] = info_sector["score"]

        resultado = calcular_score(caracteristicas)

        ranking.append({

            "ticker": accion["ticker"],

            "sector": accion["sector"],

            "score": resultado["score"],

            "motivos": resultado["motivos"]

        })

    ranking = seleccionar_mejores(

        ranking,

        minimo=radar["min_score"],

        limite=radar["top"]

    )

    return ranking
