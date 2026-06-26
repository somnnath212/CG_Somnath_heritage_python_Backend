merge_calls = 0

def merge_sort(arr):
    global merge_calls
    merge_calls += 1

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


numbers = [38, 27, 43, 3, 9, 82, 10]

sorted_numbers = merge_sort(numbers)

print("Sorted List:", sorted_numbers)
print("Total Merge Sort Recursive Calls:", merge_calls)