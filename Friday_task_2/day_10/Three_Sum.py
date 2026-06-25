def three_sum(arr):
    arr.sort()

    result = []

    for i in range(len(arr) - 2):

        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = len(arr) - 1

        while left < right:

            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result


nums = [-4, -1, -1, 0, 1, 2]

print(three_sum(nums))