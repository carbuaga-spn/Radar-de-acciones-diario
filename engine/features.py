from engine.models import Session

def calculate_features(session: Session):

    # Pattern Score
    pattern = 50

    if session.close >= session.ema9:
        pattern += 10

    if session.close >= session.vwap:
        pattern += 10

    if session.last10_volume_ratio >= 2:
        pattern += 15

    if session.close_position >= 0.90:
        pattern += 15

    session.pattern_score = min(pattern, 100)

    # Sector
    session.sector_score = session.sector_strength

    # Market
    session.market_score = session.market_strength

    # Flow
    flow = 50

    if session.last10_volume_ratio >= 3:
        flow += 25

    if session.last5_volume_ratio >= 2:
        flow += 15

    session.flow_score = min(flow, 100)

    # Risk
    risk = 80

    if session.atr > 5:
        risk -= 15

    session.risk_score = max(risk, 0)

    return session
