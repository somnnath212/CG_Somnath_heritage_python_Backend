def longest_subarray_sum_k(arr, k):

    left = 0
    window_sum = 0

    max_length = 0
    best_start = 0

    for right in range(len(arr)):

        window_sum += arr[right]

        while window_sum > k:
            window_sum -= arr[left]
            left += 1

        if right - left + 1 > max_length:
            max_length = right - left + 1
            best_start = left

    return max_length, arr[best_start:best_start + max_length]


cost = [800,1200,500,2000,600,400,1500,300,900,700]

print(longest_subarray_sum_k(cost,5000))