def max_sum_subarray(arr, k):

    n = len(arr)

    if n < k:
        return None

    window_sum = sum(arr[:k])

    max_sum = window_sum

    start = 0

    for i in range(k, n):

        window_sum += arr[i]
        window_sum -= arr[i - k]

        if window_sum > max_sum:
            max_sum = window_sum
            start = i - k + 1

    return max_sum, arr[start:start + k]


profits = [100, -50, 200, 300, -100, 400, 250, -150, 350, 500]

print(max_sum_subarray(profits, 5))