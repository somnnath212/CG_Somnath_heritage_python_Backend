balance = 1000

while True:
    print("\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            print("Balance:", balance)

        case 2:
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Updated Balance:", balance)

        case 3:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print("Updated Balance:", balance)
            else:
                print("Insufficient Balance")

        case 4:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice")