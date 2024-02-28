import random
import time
import matplotlib.pyplot as plt

def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def measure_time(algorithm, inputs):
    execution_times = []
    for inp in inputs:
        start_time = time.time()
        algorithm(inp)
        end_time = time.time()
        execution_times.append(end_time - start_time)
    return execution_times

max_input_size = 350
input_sizes = list(range(1, max_input_size + 1))

best_case_inputs = [list(range(1, n + 1)) for n in input_sizes]
worst_case_inputs = [list(range(n, 0, -1)) for n in input_sizes]
average_case_inputs = [random.sample(range(1, n + 1), n) for n in input_sizes]

plt.plot(input_sizes, measure_time(quicksort, best_case_inputs), label='Best Case')
plt.plot(input_sizes, measure_time(quicksort, worst_case_inputs), label='Worst Case')
plt.plot(input_sizes, measure_time(quicksort, average_case_inputs), label='Average Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (s)')
plt.title('Quicksort Algorithm Benchmark')
plt.legend()
plt.show()
