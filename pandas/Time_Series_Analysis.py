import pandas as pd
import numpy as np

dates = pd.date_range("2025-01-01", periods=365)

df = pd.DataFrame({
    "Date": dates,
    "Sales": np.random.randint(1000, 5000, 365)
})

df.set_index("Date", inplace=True)

# Monthly Sales
print(df.resample("M").sum())

# Weekly Average
print(df.resample("W").mean())

# Rolling Mean
df["Rolling_7"] = df["Sales"].rolling(7).mean()

# Expanding Mean
df["Expanding"] = df["Sales"].expanding().mean()

print(df.head())
