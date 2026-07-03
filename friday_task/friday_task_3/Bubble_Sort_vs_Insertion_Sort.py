arr = [45, 12, 78, 3, 29, 10]

# Bubble Sort
bubble = arr.copy()
comparisons = 0
swaps = 0

for i in range(len(bubble)):
    for j in range(len(bubble)-1-i):
        comparisons += 1
        if bubble[j] > bubble[j+1]:
            bubble[j], bubble[j+1] = bubble[j+1], bubble[j]
            swaps += 1

print("Bubble Sort")
print("Sorted:", bubble)
print("Comparisons:", comparisons)
print("Swaps:", swaps)

# Insertion Sort
insert = arr.copy()
comparisons = 0
shifts = 0

for i in range(1, len(insert)):
    key = insert[i]
    j = i - 1

    while j >= 0:
        comparisons += 1
        if insert[j] > key:
            insert[j+1] = insert[j]
            shifts += 1
            j -= 1
        else:
            break

    insert[j+1] = key

print("\nInsertion Sort")
print("Sorted:", insert)
print("Comparisons:", comparisons)
print("Shifts:", shifts)