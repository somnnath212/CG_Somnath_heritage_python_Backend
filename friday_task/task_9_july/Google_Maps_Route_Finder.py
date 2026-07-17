from collections import deque

graph = {
    "Kolkata": [("Howrah", 10), ("Durgapur", 170)],
    "Howrah": [("Kolkata", 10), ("Kharagpur", 120)],
    "Durgapur": [("Kolkata", 170), ("Asansol", 60)],
    "Kharagpur": [("Howrah", 120), ("Bhubaneswar", 280)],
    "Asansol": [("Durgapur", 60)],
    "Bhubaneswar": [("Kharagpur", 280)]
}

start = input("Enter Start City: ")
goal = input("Enter Destination City: ")

queue = deque([(start, [start], 0)])
visited = set()

found = False

while queue:

    city, path, distance = queue.popleft()

    if city == goal:
        print("\nShortest Route Found")
        print("Path:", " -> ".join(path))
        print("Distance:", distance, "km")
        found = True
        break

    if city not in visited:

        visited.add(city)

        for neighbour, dist in graph.get(city, []):
            queue.append((neighbour, path + [neighbour], distance + dist))

if not found:
    print("No Route Found")