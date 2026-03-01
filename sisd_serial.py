import time
import random

def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

def serial_matrix_add(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    operations = 0

    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
            operations += 1

    return C, operations


if __name__ == "__main__":
    size = 3   # kamu bisa ubah jadi 100, 500, dll
    A = generate_matrix(size)
    B = generate_matrix(size)

    start = time.time()
    result, ops = serial_matrix_add(A, B)
    end = time.time()

    print("=== SISD Serial Matrix Addition ===")
    print("Matrix size:", size, "x", size)
    print("Total operations:", ops)
    print("Execution time:", end - start, "seconds")