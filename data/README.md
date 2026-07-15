    # DATA MODEL

## Session

Representa una sesión completa de una acción.

Campos principales:

- ticker
- date
- sector
- industry
- open
- high
- low
- close
- volume

Mercado:

- SPY
- QQQ
- SOXX
- VIX
- DXY
- US10Y

Indicadores:

- EMA9
- EMA20
- VWAP
- ATR

Scores:

- Pattern Score
- Sector Score
- Market Score
- Flow Score
- Historical Score
- Risk Score
- Evidence Score
- Action Score

Resultados futuros:

- next_open
- next_high
- next_low
- next_close
- overnight_gap
- max_gain_next_day
- max_drawdown_next_day

Estado:

- selected_by_radar
- bought
- sold
- pnl
