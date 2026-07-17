from engine.collector import descargar_diario
from libraries.historical_library import construir
from engine.features import extraer
from engine.scorer import calcular_score
from engine.ranking import seleccionar_mejores

from engine.sector_rotation import (
    obtener_sector,
    calcular_scores_sector
)

from engine.institutional_flow import calcular_flujo


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
    # Calcular fuerza sectorial
    # =====================================

    scores_sector = calcular_scores_sector(acciones)

    # =====================================
    # FASE 3
    # Calcular flujo institucional
    # =====================================

    for accion in acciones:

        caracteristicas = accion["caracteristicas"]

        info_sector = scores_sector.get(

            accion["sector"],

            {"score": 0}

        )

        caracteristicas["sector_score"] = info_sector["score"]

        flujo = calcular_flujo(caracteristicas)

        caracteristicas["institutional_flow"] = flujo["score"]

        caracteristicas["institutional_reasons"] = flujo["motivos"]

    # =====================================
    # FASE 4
    # Score final
    # =====================================

    ranking = []

    for accion in acciones:

        caracteristicas = accion["caracteristicas"]

        resultado = calcular_score(caracteristicas)

        ranking.append({

            "ticker": accion["ticker"],

            "sector": accion["sector"],

            "score": resultado["score"],

            "motivos": resultado["motivos"],

            "institutional_flow": caracteristicas["institutional_flow"],

            "institutional_reasons": caracteristicas["institutional_reasons"]

        })

    ranking = seleccionar_mejores(

        ranking,

        minimo=radar["min_score"],

        limite=radar["top"]

    )

    return ranking