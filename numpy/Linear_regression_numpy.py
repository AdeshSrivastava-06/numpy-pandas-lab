import numpy as np
rng = np.random.default_rng(1)
X = rng.normal(size=(200,3))
true_w = np.array([2.0, -3.0,0.5])

y=X@true_w + 1.5 +rng.normal(scale = 0.3,size=200)

xb=np.c_[np.ones(len(X)),X]
w_hat = np.linalg.pinv(xb.T@xb)@xb.T@y

y_pred = xb @w_hat
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - y.mean())**2)
r2 = 1 - ss_res/ss_tot

print("Estimated weights using normal equation:", np.round(w_hat,3))
print("Intercept using normal equation:", np.round(w_hat[0],3))
print("R^2 using normal equation:", np.round(r2,4))

#by scikit learn
from sklearn.linear_model import LinearRegression
import numpy as np

rng = np.random.default_rng(1)
X = rng.normal(size=(200,3))
true_w = np.array([2.0, -3.0, 0.5])
y = X @ true_w + 1.5 + rng.normal(scale=0.3, size=200)

model = LinearRegression()
model.fit(X, y)

print("Estimated weights using scikit-learn:", np.round(model.coef_,3))
print("Intercept using scikit-learn:", np.round(model.intercept_,3))
print("R^2 using scikit-learn:", np.round(model.score(X, y), 4))
