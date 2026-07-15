from constants import *
from models import Session

def score(session: Session):

    session.action_score = (
        session.pattern_score * PATTERN +
        session.sector_score * SECTOR +
        session.flow_score * FLOW +
        session.market_score * MARKET +
        session.risk_score * RISK
    )

    if session.action_score >= 90:
        session.grade = "A+"
    elif session.action_score >= 85:
        session.grade = "A"
    elif session.action_score >= 80:
        session.grade = "B+"
    elif session.action_score >= 75:
        session.grade = "B"
    else:
        session.grade = "C"

    return session
