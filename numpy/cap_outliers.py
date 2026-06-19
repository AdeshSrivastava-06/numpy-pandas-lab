import numpy as np
x = np.array([10,11,9,10,10,1200,8,9,10], dtype=float)

median = np.median(x)
mad = np.median(np.abs(x) - median)

z_mad= 0.6745 * (x - median) / (mad if mad!=0 else 1)
mask_outlier = np.abs(z_mad)>3.5

low,high = np.percentile(x,[1,99])
x_capped = np.clip(x,low,high)

print("Outlier mask:",mask_outlier)
print("Capped series:",x_capped)