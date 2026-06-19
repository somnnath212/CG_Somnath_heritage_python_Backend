username = "admin"
password = "1234"
otp = "5678"

u = input("Enter Username: ")
p = input("Enter Password: ")

if u == username and p == password:
    entered_otp = input("Enter OTP: ")

    if entered_otp == otp:
        print("Login Successful")
    else:
        print("Invalid OTP")
else:
    print("Invalid Username or Password")