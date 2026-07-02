# merge_sort.py

def merge_sort(arr):
    # Base case: array of 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # DIVIDE: find the midpoint
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])   # Recursively sort left half
    right = merge_sort(arr[mid:])   # Recursively sort right half

    # COMBINE: merge two sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves one by one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:     # Take from left if smaller
            result.append(left[i])
            i += 1
        else:                       # Take from right otherwise
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])   # Leftover from left
    result.extend(right[j:])  # Leftover from right
    return result

data = [38, 27, 43, 3, 9, 82, 10]
print('Before:', data)
print('After: ', merge_sort(data))