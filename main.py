from engine.radar_engine import ejecutar_radar
from radars.close_radar import mostrar

from config.universe import cargar_universo
from config.radars import cargar_radar


def main():

    print()
    print("===================================")
    print("AEGIS V2")
    print("Radar Cierre")
    print("===================================")
    print()

    radar = cargar_radar("close")

    tickers = cargar_universo()

    ranking = ejecutar_radar(
        tickers,
        radar
    )

    mostrar(ranking)


if __name__ == "__main__":

    main()