import sys
import numpy as np

numbers = [1, 2, 3, 4, 5]

print(sys.getsizeof(numbers))

np_arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)

print(np_arr.nbytes)