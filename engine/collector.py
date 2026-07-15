import os
import requests

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")


def descargar_diario(symbol):

    url = (
        "https://www.alphavantage.co/query"
        "?function=TIME_SERIES_DAILY_ADJUSTED"
        f"&symbol={symbol}"
        "&outputsize=full"
        f"&apikey={API_KEY}"
    )

    r = requests.get(url, timeout=30)

    data = r.json()

    if "Time Series (Daily)" not in data:
        raise Exception(data)

    return data["Time Series (Daily)"]
