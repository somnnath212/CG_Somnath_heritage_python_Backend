import time
import numpy as np

SIZE = 1_000_000

py_list = list(range(SIZE))

start = time.time()
result = [x * 2 for x in py_list]
print("Python List:", time.time() - start)

np_arr = np.arange(SIZE)

start = time.time()
result = np_arr * 2
print("NumPy Array:", time.time() - start)