import multiprocessing
import random

def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# Algorithm 1
def sum_method_1(matrix):
    total = 0
    for row in matrix:
        for val in row:
            total += val
    return total

# Algorithm 2
def sum_method_2(matrix):
    return sum([val for row in matrix for val in row])

# Algorithm 3
def sum_method_3(matrix):
    return sum(map(sum, matrix))

# Wrapper function (IMPORTANT: no lambda)
def run_algorithm(args):
    func, matrix = args
    return func(matrix)


if __name__ == "__main__":
    n = 200
    matrix = generate_matrix(n)

    functions = [sum_method_1, sum_method_2, sum_method_3]

    with multiprocessing.Pool(3) as pool:
        results = pool.map(run_algorithm, [(f, matrix) for f in functions])

    print("=== MISD Voting Example ===")
    print("Results from 3 algorithms:", results)

    # Majority voting
    if results[0] == results[1] or results[0] == results[2]:
        final_result = results[0]
    elif results[1] == results[2]:
        final_result = results[1]
    else:
        final_result = "ERROR"

    print("Final Result after Voting:", final_result)