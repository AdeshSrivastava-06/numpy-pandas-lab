import numpy as np
X=np.array([[1.,10.,100.],
            [2.,12.,90.],
            [3.,18.,500.],
            [4.,14.,110.]])
median = np.median(X , axis=0)
q1=np.percentile(X, 25, axis=0)
q3=np.percentile(X, 75, axis=0)
iqr = np.where(q3 - q1 == 0,1,q3-q1)

X_robust = (X - median) / iqr
print("Robust - scaled features:\n" , X_robust)



import numpy as np

# Sample data (1D or multi-column allowed)
X = np.array([[1., 10., 100.],
              [2., 12., 90.],
              [3., 18., 500.],
              [4., 14., 110.]])

# Q1 (25th percentile)
q1 = np.percentile(X, 25, axis=0)

# Q3 (75th percentile)
q3 = np.percentile(X, 75, axis=0)

# IQR = Q3 - Q1
iqr = q3 - q1

print("Q1 (25th percentile):\n", q1)
print("\nQ3 (75th percentile):\n", q3)
print("\nIQR:\n", iqr)

