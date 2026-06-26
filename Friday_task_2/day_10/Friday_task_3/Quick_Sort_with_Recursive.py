quick_calls = 0

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    global quick_calls
    quick_calls += 1

    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


numbers = [38, 27, 43, 3, 9, 82, 10]

quick_sort(numbers, 0, len(numbers) - 1)

print("Sorted List:", numbers)
print("Total Quick Sort Recursive Calls:", quick_calls)