# comparison_demo.py — Benchmarking all 4 sorting algorithms
import time, random

def time_sort(func, data, *args):
    start = time.perf_counter()
    if args:
        func(data, *args)
    else:
        func(data)
    return (time.perf_counter() - start) * 1000  # milliseconds

SIZE = 1000
random_data = [random.randint(1, 10000) for _ in range(SIZE)]

tests = [
    ('Bubble Sort',    bubble_sort,    random_data.copy(),  []),
    ('Selection Sort', selection_sort, random_data.copy(),  []),
    ('Insertion Sort', insertion_sort, random_data.copy(),  []),
    ('Merge Sort',     merge_sort,     random_data.copy(),  []),
]

print(f'Sorting {SIZE} random numbers:\n')
print(f'{"Algorithm":<20} {"Time (ms)":>12}')
print('-' * 34)
for name, func, data, args in tests:
    ms = time_sort(func, data)
    print(f'{name:<20} {ms:>11.3f} ms')