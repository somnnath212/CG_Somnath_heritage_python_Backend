def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        if not swapped:
            break

    return arr


marks = [78,55,92,43,88,67,100,35]

print(bubble_sort(marks))