from collections import deque
import heapq

# ---------------- Product Class ----------------
class Product:
    def __init__(self, pid, name, category, quantity, price, warehouse):
        self.pid = pid
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.warehouse = warehouse

# ---------------- Inventory Class ----------------
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self):
        pid = input("Product ID: ")

        if pid in self.products:
            print("Product ID already exists!")
            return

        name = input("Product Name: ")
        category = input("Category: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
        warehouse = input("Warehouse: ")

        self.products[pid] = Product(
            pid, name, category, quantity, price, warehouse)

        print("Product Added Successfully!")

    def update_quantity(self):
        pid = input("Enter Product ID: ")

        if pid in self.products:
            qty = int(input("New Quantity: "))
            self.products[pid].quantity = qty
            print("Quantity Updated.")
        else:
            print("Product Not Found.")

    def remove_product(self):
        pid = input("Enter Product ID: ")

        if pid in self.products:
            del self.products[pid]
            print("Product Removed.")
        else:
            print("Product Not Found.")

    def search_product(self):
        pid = input("Enter Product ID: ")

        if pid in self.products:
            p = self.products[pid]
            print("\nProduct Details")
            print("---------------------------")
            print("ID :", p.pid)
            print("Name :", p.name)
            print("Category :", p.category)
            print("Quantity :", p.quantity)
            print("Price :", p.price)
            print("Warehouse :", p.warehouse)
        else:
            print("Product Not Found.")

    def display_products(self):
        print("\nID\tName\tCategory\tQty\tPrice\tWarehouse")

        for p in self.products.values():
            print(f"{p.pid}\t{p.name}\t{p.category}\t{p.quantity}\t{p.price}\t{p.warehouse}")

# ---------------- Order Processing ----------------
class Order:
    def __init__(self, inventory):
        self.inventory = inventory
        self.queue = []

    def place_order(self):
        pid = input("Product ID: ")
        qty = int(input("Quantity: "))
        priority = int(input("Priority (1=Highest): "))

        heapq.heappush(self.queue, (priority, pid, qty))
        print("Order Placed.")

    def process_orders(self):
        while self.queue:
            priority, pid, qty = heapq.heappop(self.queue)

            if pid not in self.inventory.products:
                print("Product Not Found.")
                continue

            product = self.inventory.products[pid]

            if product.quantity >= qty:
                product.quantity -= qty
                print("Order Processed.")
            else:
                print("Stock Unavailable.")

# ---------------- Warehouse Graph ----------------
class WarehouseGraph:
    def __init__(self):
        self.graph = {}

    def add_route(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def shortest_route(self, source, destination):

        if source not in self.graph:
            print("No Route Exists.")
            return

        queue = deque([[source]])
        visited = set()

        while queue:

            path = queue.popleft()
            node = path[-1]

            if node == destination:
                print("Shortest Route:")
                print(" -> ".join(path))
                return

            if node not in visited:
                visited.add(node)

                for neighbour in self.graph[node]:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

        print("No Route Exists.")

# ---------------- Product Report ----------------
class Report:

    def __init__(self, inventory):
        self.inventory = inventory

    def quantity_report(self):
        print("\nProducts Sorted By Quantity")

        data = sorted(
            self.inventory.products.values(),
            key=lambda x: x.quantity)

        print("ID\tName\tQty\tPrice")

        for p in data:
            print(f"{p.pid}\t{p.name}\t{p.quantity}\t{p.price}")

    def price_report(self):
        print("\nProducts Sorted By Price")

        data = sorted(
            self.inventory.products.values(),
            key=lambda x: x.price,
            reverse=True)

        print("ID\tName\tQty\tPrice")

        for p in data:
            print(f"{p.pid}\t{p.name}\t{p.quantity}\t{p.price}")

# ---------------- Main ----------------
inventory = Inventory()
orders = Order(inventory)
report = Report(inventory)
graph = WarehouseGraph()

# Sample Warehouse Routes
graph.add_route("Kolkata", "Patna")
graph.add_route("Patna", "Delhi")
graph.add_route("Delhi", "Mumbai")
graph.add_route("Mumbai", "Chennai")

while True:

    print("\n===== SMART WAREHOUSE =====")
    print("1.Add Product")
    print("2.Update Quantity")
    print("3.Remove Product")
    print("4.Search Product")
    print("5.Display Products")
    print("6.Place Order")
    print("7.Process Orders")
    print("8.Find Route")
    print("9.Quantity Report")
    print("10.Price Report")
    print("11.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        inventory.add_product()

    elif choice == "2":
        inventory.update_quantity()

    elif choice == "3":
        inventory.remove_product()

    elif choice == "4":
        inventory.search_product()

    elif choice == "5":
        inventory.display_products()

    elif choice == "6":
        orders.place_order()

    elif choice == "7":
        orders.process_orders()

    elif choice == "8":
        source = input("Source: ")
        destination = input("Destination: ")
        graph.shortest_route(source, destination)

    elif choice == "9":
        report.quantity_report()

    elif choice == "10":
        report.price_report()

    elif choice == "11":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")