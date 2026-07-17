from engine.collector import descargar_diario
from libraries.historical_library import construir
from engine.features import extraer
from engine.scorer import calcular_score
from engine.ranking import seleccionar_mejores
from radars.close_radar import mostrar

from engine.sector_rotation import (
    obtener_sector,
    score_sector
)

from config.universe import cargar_universo
from config.radars import cargar_radar


def main():

    radar = cargar_radar("close")
    tickers = cargar_universo()

    print()
    print("===================================")
    print("AEGIS V2")
    print("Radar Cierre")
    print("===================================")
    print()

    # =====================================
    # FASE 1
    # Extraer información de todas las acciones
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
    # Calcular scores
    # =====================================

    ranking = []

    for accion in acciones:

        caracteristicas = accion["caracteristicas"]

        caracteristicas["sector_score"] = score_sector(
            accion["sector"]
        )

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

    mostrar(ranking)


if __name__ == "__main__":

    main()