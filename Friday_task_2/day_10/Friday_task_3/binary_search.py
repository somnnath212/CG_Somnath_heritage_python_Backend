def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Unsorted array
numbers = [25, 8, 40, 12, 30, 18, 5]

target = 18

index = binary_search(numbers, target)

print("Index:", index)