"""
Datetime Feature Engineering using Pandas
Idea: ek single date column se multiple useful features nikalna,
jo ML models ke liye zyada informative hote hain raw date se.
"""

import pandas as pd
import numpy as np

# Step 1: Create sample sales data with dates

np.random.seed(1)
dates = pd.date_range(start="2026-01-01", periods=30, freq="D")

df = pd.DataFrame({
    "OrderDate": dates,
    "Sales": np.random.randint(1000, 5000, size=30)
})

print("Original data:\n", df.head(), "\n")


# Step 2: Extract basic date parts

df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month
df["Day"] = df["OrderDate"].dt.day
df["Weekday"] = df["OrderDate"].dt.day_name()   # e.g. Monday, Tuesday...


# Step 3: Useful flags for ML models

# dayofweek -> Monday=0 ... Sunday=6, so 5 and 6 are weekend
df["Is_Weekend"] = df["OrderDate"].dt.dayofweek.isin([5, 6])

# quarter of the year -> good for seasonal analysis
df["Quarter"] = df["OrderDate"].dt.quarter


# Step 4: Difference from a fixed reference date

reference_date = pd.to_datetime("2026-01-01")
df["Days_Since_Start"] = (df["OrderDate"] - reference_date).dt.days


# Step 5: Quick check -> average sales by weekend vs weekday

weekend_avg = df.groupby("Is_Weekend")["Sales"].mean()
print("Average sales -> Weekday vs Weekend:\n", weekend_avg, "\n")

print("Final data with new features:\n", df.head(10))

df.to_csv("sales_with_date_features.csv", index=False)
