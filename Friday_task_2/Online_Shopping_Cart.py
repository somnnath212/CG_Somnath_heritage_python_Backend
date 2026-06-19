cart = []

while True:
    print("\n1.Add Product\n2.Remove Product\n3.View Cart\n4.Checkout")
    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter product name: ")
        cart.append(item)

    elif choice == 2:
        item = input("Enter product to remove: ")
        if item in cart:
            cart.remove(item)

    elif choice == 3:
        print("Cart:", cart)

    elif choice == 4:
        cart.sort()
        print("Final Cart:", cart)
        break