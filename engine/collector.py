import os
import requests

API_KEY = os.getenv("TWELVE_DATA_API_KEY")

BASE_URL = "https://api.twelvedata.com"


def descargar_diario(symbol):

    url = (
        f"{BASE_URL}/time_series"
        f"?symbol={symbol}"
        "&interval=1day"
        "&outputsize=5000"
        "&format=JSON"
        f"&apikey={API_KEY}"
    )

    r = requests.get(url, timeout=30)

    data = r.json()

    if "values" not in data:
        raise Exception(data)

    return data["values"]