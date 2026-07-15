from models import Session
from constants import *

def score(session: Session):

    session.action_score = (
        session.pattern_score * PATTERN_WEIGHT +
        session.sector_score * SECTOR_WEIGHT +
        session.flow_score * FLOW_WEIGHT +
        session.market_score * MARKET_WEIGHT +
        session.risk_score * RISK_WEIGHT
    )

    if session.action_score >= GRADE_A_PLUS:
        session.grade = "A+"
    elif session.action_score >= GRADE_A:
        session.grade = "A"
    elif session.action_score >= GRADE_B_PLUS:
        session.grade = "B+"
    elif session.action_score >= GRADE_B:
        session.grade = "B"
    else:
        session.grade = "C"

    # Evidencias
    if session.pattern_score >= 90:
        session.evidences.append("Patrón técnico excelente")

    if session.sector_score >= 85:
        session.evidences.append("Sector líder")

    if session.flow_score >= 85:
        session.evidences.append("Flujo comprador fuerte")

    # Riesgos
    if session.market_score < 60:
        session.warnings.append("Mercado débil")

    if session.risk_score < 60:
        session.warnings.append("Riesgo elevado")

    return session