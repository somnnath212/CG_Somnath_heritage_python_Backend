def first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid          # Store current index
            right = mid - 1       # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# Driver Code
numbers = [2, 4, 4, 4, 6, 8, 10, 10, 12]

target = 4

index = first_occurrence(numbers, target)

if index != -1:
    print(f"First occurrence of {target} is at index {index}")
else:
    print("Element not found")