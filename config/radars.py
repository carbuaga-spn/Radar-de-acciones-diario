import json


def cargar_radar(nombre):

    with open("config/radars.json") as f:

        datos = json.load(f)

    return datos[nombre]
