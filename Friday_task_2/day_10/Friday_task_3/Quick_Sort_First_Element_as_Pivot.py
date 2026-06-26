def partition(arr, low, high):
    # First element is chosen as pivot
    pivot = arr[low]

    left = low + 1
    right = high

    while True:
        # Move left pointer
        while left <= right and arr[left] <= pivot:
            left += 1

        # Move right pointer
        while left <= right and arr[right] > pivot:
            right -= 1

        # If pointers cross, stop
        if left > right:
            break

        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]

    # Place pivot in its correct position
    arr[low], arr[right] = arr[right], arr[low]

    return right


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


# Driver Code
numbers = [38, 27, 43, 3, 9, 82, 10]

print("Original List:", numbers)

quick_sort(numbers, 0, len(numbers) - 1)

print("Sorted List:", numbers)