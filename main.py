from engine.models import Session
from radars.close_radar import radar

sessions = [

    Session(
        ticker="MRVL",
        pattern_score=91,
        sector_score=88,
        market_score=72,
        flow_score=90,
        risk_score=81
    ),

    Session(
        ticker="NVDA",
        pattern_score=84,
        sector_score=95,
        market_score=72,
        flow_score=80,
        risk_score=86
    ),

    Session(
        ticker="AMD",
        pattern_score=79,
        sector_score=87,
        market_score=72,
        flow_score=75,
        risk_score=84
    ),

    Session(
        ticker="UCTT",
        pattern_score=93,
        sector_score=91,
        market_score=72,
        flow_score=94,
        risk_score=82
    )

]

ranking = radar(sessions)

print("\n==============================")
print(" AEGIS - RADAR DE CIERRE")
print("==============================\n")

for i, s in enumerate(ranking, start=1):

    print(f"{i}. {s.ticker}")

    print(f"   Score : {s.action_score:.1f}")

    print(f"   Grado : {s.grade}")

    print("   Evidencias:")

    for e in s.evidences:
        print(f"      + {e}")

    if s.warnings:

        print("   Riesgos:")

        for w in s.warnings:
            print(f"      - {w}")

    print().py
