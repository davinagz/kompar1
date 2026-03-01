import multiprocessing
import time
import random

def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

def add_row(rows):
    rowA, rowB = rows
    return [a + b for a, b in zip(rowA, rowB)]

def parallel_matrix_add(A, B):
    with multiprocessing.Pool() as pool:
        result = pool.map(add_row, zip(A, B))
    return result


if __name__ == "__main__":
    n = 300  # same size as serial for comparison

    A = generate_matrix(n)
    B = generate_matrix(n)

    start = time.time()
    C = parallel_matrix_add(A, B)
    end = time.time()

    print("=== Parallel Matrix Addition ===")
    print("Matrix size:", n, "x", n)
    print("Execution time:", end - start, "seconds")