import numpy as np
X = np.array([[1.,0.,2.],
              [2.,1.,0.],
              [0.,1.,2.]])

G = X@X.T
sq_norms = np.sum(X**2 , axis=1, keepdims=True)
D2 = sq_norms + sq_norms.T - 2*G
D = np.sqrt(np.maximum(D2,0))

Xn=X/np.linalg.norm(X,axis=1,keepdims=True)
cos_sim = Xn @ Xn.T
print(D)
print(cos_sim)

#by scikit learn
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity

X = np.array([[1.,0.,2.],
              [2.,1.,0.],
              [0.,1.,2.]])

# Euclidean distance
D = euclidean_distances(X, X)

# Cosine similarity
cos_sim = cosine_similarity(X, X)

print(D)
print(cos_sim)
