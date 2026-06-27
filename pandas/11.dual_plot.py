import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate 2 years of daily data
date_rng = pd.date_range(start="2022-01-01", end="2023-12-31", freq="D")
np.random.seed(42)

sales = np.random.randint(200, 500, size=len(date_rng)) + np.sin(np.linspace(0, 20, len(date_rng))) * 50

#har din ka profit 10% ke aas paas rahega, lekin thoda upar-niche
profit = sales * (0.1 + np.random.normal(0,0.02,len(date_rng)))

df=pd.DataFrame({"Date":date_rng, "Sales":sales, "Profit": profit})

#resample to monthly i.e monthly grouping
monthly = df.resample("ME", on="Date").sum()

fig , ax1=plt.subplots(figsize=(12,7))

# Left y-axis = Sales
ax1.plot(monthly.index, monthly["Sales"], color="blue", label="Sales", linewidth=2)
ax1.set_ylabel("Sales (₹)", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Right y-axis = Profit
ax2 = ax1.twinx()
ax2.plot(monthly.index, monthly["Profit"], color="green", linestyle="--", label="Profit", linewidth=2)
ax2.set_ylabel("Profit (₹)", color="green")
ax2.tick_params(axis="y", labelcolor="green")

# Title & Legends
plt.title("Monthly Sales vs Profit (Dual-Axis on Large Data)", fontsize=14)
fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9))
plt.show()
