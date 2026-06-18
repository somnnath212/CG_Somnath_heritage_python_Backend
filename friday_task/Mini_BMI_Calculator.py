# Calculate BMI

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")