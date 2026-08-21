import numpy as np

# fake user-item ratings matrix (rows=users, cols=movies), 0 means not rated
R = np.array([
    [5, 3, 0, 1, 4],
    [4, 0, 0, 1, 3],
    [1, 1, 0, 5, 0],
    [0, 0, 5, 4, 0],
    [0, 1, 5, 4, 0],
    [5, 0, 3, 0, 4],
])

n_users, n_items = R.shape
k = 3  # number of latent factors (hidden traits like "likes action" etc)

np.random.seed(42)
P = np.random.normal(scale=0.1, size=(n_users, k))  # user factors
Q = np.random.normal(scale=0.1, size=(n_items, k))  # item factors

mask = R > 0  # only train on observed ratings

def train(R, P, Q, mask, lr=0.01, reg=0.02, epochs=2000):
    losses = []
    for epoch in range(epochs):
        pred = P @ Q.T
        error = mask * (R - pred)

        # gradients w.r.t P and Q, with L2 regularization to avoid overfitting
        dP = -2 * error @ Q + 2 * reg * P
        dQ = -2 * error.T @ P + 2 * reg * Q

        P -= lr * dP
        Q -= lr * dQ

        loss = np.sum((mask * (R - P @ Q.T)) ** 2) + reg * (np.sum(P**2) + np.sum(Q**2))
        losses.append(loss)

        if epoch % 200 == 0:
            print(f"epoch {epoch}, loss {loss:.4f}")

    return P, Q, losses

P, Q, losses = train(R, P, Q, mask, lr=0.01, reg=0.02, epochs=2000)

R_pred = P @ Q.T

print("\noriginal ratings matrix:")
print(R)

print("\npredicted ratings matrix (rounded):")
print(np.round(R_pred, 2))

# for each user, recommend the top unrated item
print("\nrecommendations:")
for user in range(n_users):
    unrated = np.where(R[user] == 0)[0]
    if len(unrated) == 0:
        print(f"user {user}: no unrated items left")
        continue
    best_item = unrated[np.argmax(R_pred[user, unrated])]
    print(f"user {user}: recommend item {best_item} (predicted rating {R_pred[user, best_item]:.2f})")

# rmse on observed entries, to sanity check how well it fit known ratings
rmse = np.sqrt(np.sum((mask * (R - R_pred)) ** 2) / np.sum(mask))
print(f"\ntrain RMSE on known ratings: {rmse:.4f}")
