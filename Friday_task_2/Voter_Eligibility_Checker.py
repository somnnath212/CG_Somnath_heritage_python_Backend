age = int(input("Enter Age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18:
    if citizen.lower() == "yes":
        print("Eligible to Vote")
    else:
        print("Not Eligible - Not a Citizen")
else:
    print("Not Eligible - Underage")