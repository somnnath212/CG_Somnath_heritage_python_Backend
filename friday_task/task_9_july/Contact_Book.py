contacts = {}

while True:

    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        contacts[name] = phone
        print("Contact Added Successfully.")

    elif choice == "2":
        name = input("Enter Name: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact Not Found.")

    elif choice == "3":
        name = input("Enter Name: ")

        if name in contacts:
            phone = input("Enter New Phone Number: ")
            contacts[name] = phone
            print("Contact Updated.")
        else:
            print("Contact Not Found.")

    elif choice == "4":
        name = input("Enter Name: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted.")
        else:
            print("Contact Not Found.")

    elif choice == "5":
        print("\nAll Contacts")

        if not contacts:
            print("No Contacts Available")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")