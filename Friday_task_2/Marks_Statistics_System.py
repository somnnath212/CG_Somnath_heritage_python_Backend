marks = []

n = int(input("How many marks? "))

for i in range(n):
    marks.append(int(input("Enter mark: ")))

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)
pass_count = len([m for m in marks if m >= 40])

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Pass Count:", pass_count)