"""
stats_calc.py
Quick descriptive statistics on a numeric dataset using NumPy.
"""

import numpy as np

def describe(data: list) -> dict:
    arr = np.array(data, dtype=np.float64)

    return {
        "count": arr.size,
        "mean": np.mean(arr),
        "median": np.median(arr),
        "std_dev": np.std(arr),
        "variance": np.var(arr),
        "min": np.min(arr),
        "max": np.max(arr),
        "range": np.max(arr) - np.min(arr)
    }


if __name__ == "__main__":
    sample_data = [12, 15, 22, 8, 19, 25, 14, 30, 5, 18]

    stats = describe(sample_data)

    print("Dataset:", sample_data)
    print("\n--- Statistics ---")
    for key, value in stats.items():
        print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")