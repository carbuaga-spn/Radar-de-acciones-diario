import json


def cargar_universo():

    with open("config/universe.json") as f:

        return json.load(f)
