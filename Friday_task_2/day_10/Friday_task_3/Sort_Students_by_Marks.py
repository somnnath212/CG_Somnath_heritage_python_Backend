def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["marks"] <= right[j]["marks"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2

    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    return merge(left, right)


# Driver Code
students = [
    {"roll": 101, "name": "Arjun", "marks": 88},
    {"roll": 102, "name": "Priya", "marks": 95},
    {"roll": 103, "name": "Rahul", "marks": 72},
    {"roll": 104, "name": "Sneha", "marks": 91},
    {"roll": 105, "name": "Vikram", "marks": 68},
    {"roll": 106, "name": "Deepika", "marks": 84}
]

sorted_students = merge_sort(students)

print("Students Sorted by Marks (Ascending):")
for student in sorted_students:
    print(student)