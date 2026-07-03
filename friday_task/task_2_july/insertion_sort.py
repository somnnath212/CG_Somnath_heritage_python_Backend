# insertion_sort.py

def insertion_sort(arr):
    for i in range(1, len(arr)):       # Start from 2nd element
        key = arr[i]                   # Element to be inserted
        j = i - 1                      # Start comparing from left

        # Shift elements greater than key one position right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key               # Insert key in correct spot
    return arr

# Verbose version — shows each step
def insertion_sort_verbose(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(f'  After inserting {key}: {arr}')
    return arr

nums = [5, 3, 8, 4, 2]
print('Original:', nums)
result = insertion_sort_verbose(nums)
print('Sorted:  ', result)