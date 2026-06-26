def merge_sort(arr):
    # Print the current array before splitting
    print("Splitting:", arr)

    # Base case
    if len(arr) <= 1:
        return arr

    # Find the middle
    mid = len(arr) // 2

    # Recursively split
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    merged = merge(left, right)

    # Print after merging
    print("Merging :", left, "+", right, "=", merged)

    return merged


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

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Driver Code
numbers = [38, 27, 43, 3, 9, 82, 10]

print("Original List:", numbers)
sorted_numbers = merge_sort(numbers)
print("\nFinal Sorted List:", sorted_numbers)