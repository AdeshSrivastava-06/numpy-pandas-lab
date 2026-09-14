"""
np.einsum — Einstein summation notation.
One of NumPy's most powerful (and underused) features: lets you express
dot products, transposes, traces, outer products, and batched matrix ops
all with a single concise notation, often faster than chaining separate calls.
"""

import numpy as np
import time


def demo_basic_ops():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("Vectors a, b:", a, b)

    # dot product
    print("dot product      :", np.einsum('i,i->', a, b), "== ", np.dot(a, b))

    # outer product
    print("outer product:\n", np.einsum('i,j->ij', a, b))

    # element-wise multiply
    print("elementwise mul  :", np.einsum('i,i->i', a, b))


def demo_matrix_ops():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("\nMatrix A:\n", A)
    print("Matrix B:\n", B)

    # matrix multiplication
    print("A @ B via einsum:\n", np.einsum('ij,jk->ik', A, B))
    print("A @ B via matmul:\n", A @ B)

    # transpose
    print("transpose(A):\n", np.einsum('ij->ji', A))

    # trace
    print("trace(A):", np.einsum('ii->', A))

    # sum all elements
    print("sum(A):", np.einsum('ij->', A))

    # row sums / column sums
    print("row sums:", np.einsum('ij->i', A))
    print("col sums:", np.einsum('ij->j', A))


def demo_batched_matmul():
    # batch of 3 matrices, each 2x2 — a common pattern in deep learning
    batch = np.random.default_rng(0).integers(1, 5, size=(3, 2, 2))
    print("\nBatch of matrices, shape:", batch.shape)

    # batched matmul: batch @ batch (per-sample)
    result = np.einsum('bij,bjk->bik', batch, batch)
    print("Batched A@A result shape:", result.shape)


def speed_comparison():
    rng = np.random.default_rng(1)
    A = rng.random((500, 500))
    B = rng.random((500, 500))

    start = time.time()
    for _ in range(50):
        _ = A @ B
    t_matmul = time.time() - start

    start = time.time()
    for _ in range(50):
        _ = np.einsum('ij,jk->ik', A, B)
    t_einsum = time.time() - start

    print(f"\n@ operator time : {t_matmul:.4f}s")
    print(f"einsum time     : {t_einsum:.4f}s")
    print("(einsum is flexible, not always fastest — matmul uses optimized BLAS)")


if __name__ == "__main__":
    demo_basic_ops()
    demo_matrix_ops()
    demo_batched_matmul()
    speed_comparison()
