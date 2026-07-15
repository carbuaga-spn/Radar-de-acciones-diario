from dataclasses import dataclass

@dataclass
class Session:
    ticker: str

    pattern_score: float
    sector_score: float
    market_score: float
    flow_score: float
    risk_score: float

    action_score: float = 0
    grade: str = ""
