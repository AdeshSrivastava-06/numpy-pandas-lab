import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Generate data with anomalies
np.random.seed(42)
date_rng = pd.date_range(start="2020-01-01", periods=48, freq='ME')
trend = np.linspace(100, 200, len(date_rng))
seasonality = 15 * np.sin(2 * np.pi * date_rng.month.values / 12)
noise = np.random.normal(0, 5, len(date_rng))
sales = trend + seasonality + noise

# Inject anomalies (spikes)
sales[10] += 60
sales[25] -= 40

df = pd.DataFrame({'Date': date_rng, 'Sales': sales}).set_index('Date')

# Seasonal decomposition
result = seasonal_decompose(df['Sales'], model='additive', period=12)
residual = result.resid.dropna()

# Detect anomalies (residuals outside ±2 std dev)
threshold = 2 * residual.std()
anomalies = residual[(abs(residual) > threshold)]

# Plot decomposition
result.plot()
plt.show()

# Plot anomalies
plt.figure(figsize=(12,6))
plt.plot(df.index, df['Sales'], label="Observed", color="blue")
plt.scatter(anomalies.index, df.loc[anomalies.index, 'Sales'], color="red", marker="o", s=100, label="Anomaly")
plt.title("Sales with Anomalies Detected (via Seasonal Decomposition Residuals)")
plt.legend()
plt.show()
