import time
import random
import multiprocessing

def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# Serial version
def serial_matrix_add(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

# Parallel version
def add_row(rows):
    rowA, rowB = rows
    return [a + b for a, b in zip(rowA, rowB)]

def parallel_matrix_add(A, B):
    with multiprocessing.Pool() as pool:
        result = pool.map(add_row, zip(A, B))
    return result


if __name__ == "__main__":
    size = 300

    A = generate_matrix(size)
    B = generate_matrix(size)

    # Measure serial
    start = time.time()
    serial_matrix_add(A, B)
    serial_time = time.time() - start

    # Measure parallel
    start = time.time()
    parallel_matrix_add(A, B)
    parallel_time = time.time() - start

    speedup = serial_time / parallel_time

    print("Matrix size:", size, "x", size)
    print("Serial time:", serial_time)
    print("Parallel time:", parallel_time)
    print("Speedup:", speedup)