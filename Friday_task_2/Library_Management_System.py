books = {
    "Python": 5,
    "Java": 3,
    "C++": 2
}

while True:
    print("\n1.Search\n2.Add\n3.Issue\n4.Return\n5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Book Name: ")
        if book in books:
            print("Available Copies:", books[book])
        else:
            print("Book Not Found")

    elif choice == 2:
        book = input("Book Name: ")
        qty = int(input("Quantity: "))
        books[book] = qty

    elif choice == 3:
        book = input("Book Name: ")
        if book in books and books[book] > 0:
            books[book] -= 1
            print("Book Issued")
        else:
            print("Not Available")

    elif choice == 4:
        book = input("Book Name: ")
        if book in books:
            books[book] += 1

    elif choice == 5:
        break