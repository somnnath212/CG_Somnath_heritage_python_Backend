graph = {
    "Alice": ["Bob"],
    "Bob": ["Alice"]
}

person1 = "Alice"
person2 = "Charlie"

graph.setdefault(person1, []).append(person2)
graph.setdefault(person2, []).append(person1)

print(graph)