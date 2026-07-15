import json
import os


def guardar_json(nombre, datos):

    os.makedirs("data", exist_ok=True)

    ruta = f"data/{nombre}.json"

    with open(ruta, "w", encoding="utf8") as f:
        json.dump(datos, f, indent=4)
