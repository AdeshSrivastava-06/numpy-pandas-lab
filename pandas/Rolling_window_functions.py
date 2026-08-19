import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2026-01-01", periods=90, freq="D")
sales = np.random.randint(200, 1000, size=90) + np.sin(np.linspace(0, 15, 90)) * 100

df = pd.DataFrame({"date": dates, "sales": sales.round(2)})
df.set_index("date", inplace=True)

print(df.head())

# moving average and volatility
df["rolling_mean_7"] = df["sales"].rolling(window=7).mean()
df["rolling_std_7"] = df["sales"].rolling(window=7).std()
df["rolling_mean_7_partial"] = df["sales"].rolling(window=7, min_periods=1).mean()

# cumulative stats
df["expanding_mean"] = df["sales"].expanding().mean()
df["expanding_max"] = df["sales"].expanding().max()

# more weight to recent values
df["ewm_mean_span5"] = df["sales"].ewm(span=5, adjust=False).mean()

# custom rolling function
df["rolling_range_5"] = df["sales"].rolling(window=5).apply(lambda x: x.max() - x.min())

# rolling correlation
df["marketing_spend"] = np.random.randint(50, 300, size=90).astype(float)
df["rolling_corr_14"] = df["sales"].rolling(window=14).corr(df["marketing_spend"])

# spike detection using rolling mean +- 2 std
df["upper_bound"] = df["rolling_mean_7"] + 2 * df["rolling_std_7"]
df["lower_bound"] = df["rolling_mean_7"] - 2 * df["rolling_std_7"]
df["is_spike"] = (df["sales"] > df["upper_bound"]) | (df["sales"] < df["lower_bound"])

print(df[df["is_spike"]][["sales", "rolling_mean_7", "is_spike"]])

# resample to weekly, then rolling on top
weekly_sales = df["sales"].resample("W").sum()
weekly_rolling_mean = weekly_sales.rolling(window=3).mean()

weekly_summary = pd.DataFrame({
    "weekly_sales": weekly_sales,
    "rolling_3week_mean": weekly_rolling_mean
})
print(weekly_summary)
