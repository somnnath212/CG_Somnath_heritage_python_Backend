def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr


employee = [1001,1003,1007,1012,1020]

employee.append(1008)

print(insertion_sort(employee))