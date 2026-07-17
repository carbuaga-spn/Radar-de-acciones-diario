def calcular_flujo(caracteristicas):

    score = 0
    motivos = []

    # =====================================
    # Volumen relativo
    # =====================================

    if caracteristicas["relative_volume"] >= 2.0:

        score += 30
        motivos.append("Volumen excepcional")

    elif caracteristicas["relative_volume"] >= 1.5:

        score += 20
        motivos.append("Volumen muy alto")

    elif caracteristicas["relative_volume"] >= 1.2:

        score += 10
        motivos.append("Volumen alto")

    # =====================================
    # Cierre cerca del máximo
    # =====================================

    if caracteristicas["close_position"] >= 0.90:

        score += 20
        motivos.append("Cierre en máximos")

    elif caracteristicas["close_position"] >= 0.80:

        score += 10
        motivos.append("Cierre fuerte")

    # =====================================
    # Cuerpo dominante
    # =====================================

    if caracteristicas["body_percent"] >= 0.70:

        score += 20
        motivos.append("Cuerpo dominante")

    elif caracteristicas["body_percent"] >= 0.60:

        score += 10
        motivos.append("Buen cuerpo")

    # =====================================
    # Tendencia
    # =====================================

    if caracteristicas["above_ema20"]:

        score += 15

    if caracteristicas["above_ema9"]:

        score += 5

    return {

        "score": score,

        "motivos": motivos

    }
