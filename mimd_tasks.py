import multiprocessing
import random

def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

def task_sum(matrix):
    return sum(map(sum, matrix))

def task_find_max(matrix):
    return max([max(row) for row in matrix])

def task_count_even(matrix):
    count = 0
    for row in matrix:
        for val in row:
            if val % 2 == 0:
                count += 1
    return count

def task_transpose(matrix):
    return list(zip(*matrix))

def run_task(args):
    func, matrix = args
    return func(matrix)


if __name__ == "__main__":
    n = 200
    matrix = generate_matrix(n)

    tasks = [task_sum, task_find_max, task_count_even, task_transpose]

    with multiprocessing.Pool(4) as pool:
        results = pool.map(run_task, [(t, matrix) for t in tasks])

    print("=== MIMD Example ===")
    print("Total Sum:", results[0])
    print("Max Value:", results[1])
    print("Even Count:", results[2])
    print("Transpose (first row):", results[3][0])