products = (
    ("Laptop", 50000),
    ("Mobile", 20000),
    ("Headphone", 3000),
    ("Tablet", 25000)
)

budget = int(input("Enter Budget: "))

print("Products above budget:")

for product, price in products:
    if price > budget:
        print(product, "-", price)