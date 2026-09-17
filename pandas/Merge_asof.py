"""
pandas merge_asof() — Time-Aware Nested Joins

pd.merge() (exact key match). 
merge_asof():-
matches on the NEAREST prior (or nearest, or nearest-after) key,
which is essential for time-series data where timestamps rarely
line up exactly.

Classic use case: matching stock TRADES to the most recent QUOTE
available at that instant — you can't join on exact timestamp
because trades and quotes are logged independently.
"""

import pandas as pd

# 1. Quotes: bid/ask prices logged at irregular times
quotes = pd.DataFrame({
    "timestamp": pd.to_datetime([
        "2024-01-01 09:00:00.020",
        "2024-01-01 09:00:00.045",
        "2024-01-01 09:00:00.075",
        "2024-01-01 09:00:00.120",
    ]),
    "ticker": ["AAPL"] * 4,
    "bid": [100.10, 100.12, 100.15, 100.14],
    "ask": [100.15, 100.17, 100.20, 100.18],
})


# 2. Trades: executed at their own irregular times

trades = pd.DataFrame({
    "timestamp": pd.to_datetime([
        "2024-01-01 09:00:00.030",
        "2024-01-01 09:00:00.050",
        "2024-01-01 09:00:00.100",
        "2024-01-01 09:00:00.130",
    ]),
    "ticker": ["AAPL"] * 4,
    "price": [100.13, 100.16, 100.19, 100.17],
    "size": [200, 100, 300, 150],
})

# Both sides MUST be sorted by the merge key
quotes = quotes.sort_values("timestamp")
trades = trades.sort_values("timestamp")

# 3. merge_asof: attach the most recent quote AT OR BEFORE

#    each trade (direction="backward" is the default)
merged = pd.merge_asof(
    trades,
    quotes,
    on="timestamp",
    by="ticker",              # like a groupby key within the asof match
    direction="backward",     # "forward" or "nearest" also available
    tolerance=pd.Timedelta("50ms"),  # refuse matches older than this
)

merged["mid_price"] = (merged["bid"] + merged["ask"]) / 2
merged["trade_vs_mid"] = merged["price"] - merged["mid_price"]

print("Trades matched with most recent quote:\n")
print(merged)


# 4. Why this matters vs a normal merge

print("\n--- Compare: a normal merge() would require EXACT timestamp")
print("    matches and drop every row here (zero overlap). ---")
exact = pd.merge(trades, quotes, on=["timestamp", "ticker"], how="inner")
print(f"Rows matched by exact merge(): {len(exact)}")
print(f"Rows matched by merge_asof():  {len(merged.dropna(subset=['bid']))}")
