def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return None


prices = [150, 250, 350, 400, 500, 600, 750, 850]

pair = two_sum_sorted(prices, 1000)

print(pair)