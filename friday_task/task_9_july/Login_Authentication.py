users = {
    "admin": "1234",
    "student": "abcd"
}

username = input("Username: ")
password = input("Password: ")

if users.get(username) == password:
    print("Login Successful")
else:
    print("Invalid Credentials")