# Run 3 math functions (tasks) in parallel
# Based on the following tutorial: https://www.youtube.com/watch?v=GT10PnUFLlE

import multiprocessing as mp
import time
import math

results_a = []
results_b = []
results_c = []


def make_calculation_one(numbers):
    print("Function (1) Time started:", time.time())
    for number in numbers:
        results_a.append(math.sqrt(number ** 3))


def make_calculation_two(numbers):
    print("Function (2) Time started:", time.time())
    for number in numbers:
        results_a.append(math.sqrt(number ** 4))


def make_calculation_three(numbers):
    print("Function (3) Time started:", time.time())
    for number in numbers:
        results_a.append(math.sqrt(number ** 5))


def sequential_execution():
    number_list = list(range(5000000))

    start = time.time()
    make_calculation_one(number_list)
    make_calculation_two(number_list)
    make_calculation_three(number_list)

    end = time.time()
    return(end - start)

def parallel_execution():
    number_list = list(range(5000000))
    p1 = mp.Process(target=make_calculation_one, args=(number_list,))
    p2 = mp.Process (target=make_calculation_two, args=(number_list,))
    p3 = mp.Process (target=make_calculation_three, args=(number_list,))
    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()
    return (end - start)

def init_function():
    if __name__ == '__main__':
        print("Sequential Execution Time:",sequential_execution())
        print("Parallel Execution Time:",parallel_execution())

init_function()