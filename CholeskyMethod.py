def cholesky_decomposition(A):
    """Performs Cholesky decomposition on a symmetric positive-definite matrix A.

    Args:
        A (list of lists): The matrix to decompose, represented as a nested list.

    Returns:
        L (list of lists): The lower triangular matrix from the decomposition.
    """
    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            sum_k = sum(L[i][k] * L[j][k] for k in range(j))

            if i == j:  # Diagonal elements
                L[i][j] = (A[i][i] - sum_k) ** 0.5
            else:
                L[i][j] = (A[i][j] - sum_k) / L[j][j]
    return L


# Example Usage
def main():
    A = [
        [25, 15, -5],
        [15, 18, 0],
        [-5, 0, 11]
    ]

    L = cholesky_decomposition(A)

    print("L = ")
    for row in L:
        print(row)


if __name__ == "__main__":
    main()
