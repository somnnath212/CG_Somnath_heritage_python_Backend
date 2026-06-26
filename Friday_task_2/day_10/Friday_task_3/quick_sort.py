def partition(arr, low, high):
    # Last element is chosen as pivot
    pivot = arr[high]

    i = low - 1

    # Rearrange elements around the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Partition the array
        pivot_index = partition(arr, low, high)

        # Recursively sort left and right subarrays
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


# Driver Code
numbers = [38, 27, 43, 3, 9, 82, 10]

print("Original List:", numbers)

quick_sort(numbers, 0, len(numbers) - 1)

print("Sorted List:", numbers)