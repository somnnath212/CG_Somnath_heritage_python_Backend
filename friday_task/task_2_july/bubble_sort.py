# bubble_sort.py

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # Outer loop: n passes
        swapped = False
        for j in range(0, n-i-1):  # Inner loop: shrinks each pass
            if arr[j] > arr[j+1]:  # Compare adjacent
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        if not swapped:          # Optimization: stop early if sorted
            break
    return arr

# ── Test ──
numbers = [64, 34, 25, 12, 22]
print('Before:', numbers)
print('After: ', bubble_sort(numbers))