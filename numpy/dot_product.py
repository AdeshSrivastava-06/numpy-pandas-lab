import numpy as np

# Define three vector
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(np.dot(A, B))
print(A@B)

import numpy as np

# Define three vectors
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.array([7, 8, 9])

# Calculate dot product using numpy.dot() function
dot_product_AB = np.dot(A, B)
dot_product_BA = np.dot(B, A)

print(dot_product_AB)
print(dot_product_BA)

# Check commutative property: A • B = B • A
if dot_product_AB == dot_product_BA:
    print("The dot product is commutative.")
else:
    print("The dot product is not commutative.")
    
# Check distributive property: A • (B + C) = A • B + A • C
dot_product_A_BC = np.dot(A, B + C)
dot_product_AB_plus_AC = np.dot(A, B) + np.dot(A, C)

print(dot_product_A_BC)
print(dot_product_AB_plus_AC)


if dot_product_A_BC == dot_product_AB_plus_AC:
    print("The dot product is distributive.")
else:
    print("The dot product is not distributive.")
