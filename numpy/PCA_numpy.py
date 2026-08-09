"""
PCA (Principal Component Analysis) from scratch using NumPy 
Idea: reduce high-dimensional data to fewer dimensions while keeping
most of the variance (information) intact.
"""

import numpy as np
import matplotlib.pyplot as plt


# Step 1: Generate sample data (correlated features)

np.random.seed(42)
x = np.random.randn(200)
y = 2 * x + np.random.randn(200) * 0.5   # y depends on x -> correlated
data = np.column_stack([x, y])            # shape -> (200, 2)



# Step 2: PCA function

def pca(X, n_components):
    # 1. Mean-center the data (PCA needs data centered at origin)
    mean = X.mean(axis=0)
    X_centered = X - mean

    # 2. Covariance matrix -> tells how features vary together
    #    rowvar=False because our columns are features, rows are samples
    cov_matrix = np.cov(X_centered, rowvar=False)

    # 3. Eigen decomposition -> eigenvectors = directions of max variance
    #                           eigenvalues  = amount of variance in that direction
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # 4. Sort eigenvectors by eigenvalues in descending order
    #    (biggest variance direction should come first)
    sorted_idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_idx]
    eigenvectors = eigenvectors[:, sorted_idx]

    # 5. Pick top n_components eigenvectors -> these become new axes
    components = eigenvectors[:, :n_components]

    # 6. Project original data onto these new axes
    X_reduced = X_centered @ components

    # how much variance each component explains (useful info)
    explained_variance_ratio = eigenvalues[:n_components] / eigenvalues.sum()

    return X_reduced, components, explained_variance_ratio


# Step 3: Run PCA -reduce 2D data to 1D

X_reduced, components, variance_ratio = pca(data, n_components=1)

print("Principal component (direction of max variance):\n", components)
print("Variance explained by this component:", variance_ratio[0] * 100, "%")


# Step 4: Visualize original vs reduced data

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].scatter(data[:, 0], data[:, 1], alpha=0.6)
axes[0].set_title("Original 2D data")

axes[1].scatter(X_reduced, np.zeros_like(X_reduced), alpha=0.6, color='orange')
axes[1].set_title("Reduced to 1D using PCA")

plt.tight_layout()
plt.savefig("pca_output.png")
plt.show()
