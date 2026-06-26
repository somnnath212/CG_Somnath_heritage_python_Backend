def find_unique_pairs(arr, target):
    left = 0
    right = len(arr) - 1
    pairs = []

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            pairs.append((arr[left], arr[right]))

            # Skip duplicate values
            left_value = arr[left]
            right_value = arr[right]

            while left < right and arr[left] == left_value:
                left += 1

            while left < right and arr[right] == right_value:
                right -= 1

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return pairs


# Driver Code
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8]
target = 8

result = find_unique_pairs(numbers, target)

print("Unique pairs with sum", target, "are:")
for pair in result:
    print(pair)