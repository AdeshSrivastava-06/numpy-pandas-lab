"""
K-Means Clustering from scratch using NumPy (no sklearn)
Idea: group data points into 'k' clusters based on distance to centroids.
"""

import numpy as np
import matplotlib.pyplot as plt


# Step 1: Generate sample data (3 blobs of points)
np.random.seed(42)
cluster1 = np.random.randn(50, 2) + np.array([0, 0])
cluster2 = np.random.randn(50, 2) + np.array([6, 6])
cluster3 = np.random.randn(50, 2) + np.array([0, 6])
data = np.vstack([cluster1, cluster2, cluster3])   # shape -> (150, 2)


# Step 2: K-Means function
def kmeans(X, k, max_iters=100, tol=1e-4):
    n_samples, n_features = X.shape

    # randomly pick k points from data as initial centroids
    random_idx = np.random.choice(n_samples, k, replace=False)
    centroids = X[random_idx]

    for iteration in range(max_iters):
        #  Assignment step 
        # distance of every point from every centroid (broadcasting magic)
        # X[:, np.newaxis] shape -> (n_samples, 1, n_features)
        # centroids shape       -> (k, n_features)
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)  # (n_samples, k)
        labels = np.argmin(distances, axis=1)  # closest centroid index for each point

        #  Update step 
        new_centroids = np.array([
            X[labels == i].mean(axis=0) if np.any(labels == i) else centroids[i]
            for i in range(k)
        ])

        #  Convergence check 
        shift = np.linalg.norm(new_centroids - centroids)
        centroids = new_centroids

        if shift < tol:
            print(f"Converged in {iteration + 1} iterations")
            break

    return centroids, labels


# Step 3: Run K-Means with k=3
k = 3
final_centroids, final_labels = kmeans(data, k)

print("Final centroids:\n", final_centroids)


# Step 4: Visualize the clusters
colors = ['red', 'green', 'blue']
for i in range(k):
    points = data[final_labels == i]
    plt.scatter(points[:, 0], points[:, 1], c=colors[i], label=f'Cluster {i}')

plt.scatter(final_centroids[:, 0], final_centroids[:, 1],
            c='black', marker='X', s=200, label='Centroids')
plt.title("K-Means Clustering from scratch (NumPy)")
plt.legend()
plt.savefig("kmeans_output.png")
plt.show()
