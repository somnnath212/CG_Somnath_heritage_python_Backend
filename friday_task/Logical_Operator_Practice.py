# Check club access

age = int(input("Enter your age: "))
membership_status = input("Enter membership status (True/False): ")

membership_status = membership_status == "True"

can_access = age >= 18 and membership_status

print(f"Can access special club: {can_access}")