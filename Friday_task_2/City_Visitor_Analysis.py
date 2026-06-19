cities = []

n = int(input("How many city names? "))

for i in range(n):
    city = input("Enter city name: ")
    cities.append(city)

unique_cities = set(cities)

print("All Cities:", cities)
print("Unique Cities:", unique_cities)
print("Number of Unique Cities:", len(unique_cities))