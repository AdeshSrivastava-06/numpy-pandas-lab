import numpy as np

# Monte Carlo Simulation using NumPy
# Estimate the value of Pi and analyze simulation accuracy

np.random.seed(42)


def estimate_pi(n_samples):
    """
    Estimate Pi using the Monte Carlo method.

    Random points are generated inside a square.
    Points inside the quarter circle are counted.
    """

    points = np.random.uniform(-1, 1, size=(n_samples, 2))

    # Calculate distance from origin
    distance_squared = np.sum(points ** 2, axis=1)

    # Points inside the unit circle
    inside_circle = distance_squared <= 1

    # Pi = 4 * ratio of points inside circle
    pi_estimate = 4 * np.mean(inside_circle)

    return pi_estimate


# Different sample sizes
sample_sizes = [100, 1_000, 10_000, 100_000, 1_000_000]

print("Monte Carlo Pi Estimation")
print("-" * 40)

for n in sample_sizes:
    estimated_pi = estimate_pi(n)
    error = abs(np.pi - estimated_pi)

    print(f"Samples       : {n:,}")
    print(f"Estimated Pi  : {estimated_pi:.6f}")
    print(f"Actual Pi     : {np.pi:.6f}")
    print(f"Absolute Error: {error:.6f}")
    print("-" * 40)


# Simulation of multiple experiments

experiments = 20
n_samples = 100_000

results = np.array([
    estimate_pi(n_samples)
    for _ in range(experiments)
])

print("\nMultiple Simulation Results")
print("-" * 40)

print(f"Mean Estimate : {np.mean(results):.6f}")
print(f"Std Deviation : {np.std(results):.6f}")
print(f"Minimum       : {np.min(results):.6f}")
print(f"Maximum       : {np.max(results):.6f}")

# Difference from actual Pi
errors = np.abs(results - np.pi)

print(f"Mean Error    : {np.mean(errors):.6f}")
print(f"Best Error    : {np.min(errors):.6f}")


# Vectorized simulation
n = 500_000

points = np.random.uniform(-1, 1, size=(n, 2))

x = points[:, 0]
y = points[:, 1]

inside = (x ** 2 + y ** 2) <= 1

inside_count = np.sum(inside)
outside_count = n - inside_count

print("\nPoint Distribution")
print("-" * 40)
print(f"Inside Circle : {inside_count:,}")
print(f"Outside       : {outside_count:,}")
print(f"Estimated Pi  : {4 * inside_count / n:.6f}")
