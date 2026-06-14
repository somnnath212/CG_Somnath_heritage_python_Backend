# Find the larger number

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

if first_number > second_number:
    print(f"{first_number} is larger.")
elif second_number > first_number:
    print(f"{second_number} is larger.")
else:
    print("Both numbers are equal.")