from engine.collector import descargar_diario

TICKERS = [
    "NVDA",
    "AMD",
    "AVGO",
    "MRVL",
    "TSM"
]

print("=== Descargando históricos ===")

for ticker in TICKERS:
    try:
        datos = descargar_diario(ticker)
        print(f"{ticker}: {len(datos)} sesiones descargadas")
    except Exception as e:
        print(f"{ticker}: ERROR -> {e}")

print("Proceso terminado.")