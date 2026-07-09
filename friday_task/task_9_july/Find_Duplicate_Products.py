products = [
    "Laptop",
    "Mouse",
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor"
]

seen = set()
duplicates = set()

for product in products:

    if product in seen:
        duplicates.add(product)
    else:
        seen.add(product)

print(duplicates)