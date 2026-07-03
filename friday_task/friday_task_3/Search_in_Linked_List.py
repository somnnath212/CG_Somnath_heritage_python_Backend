class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(25)
head.next.next = Node(45)
head.next.next.next = Node(60)

key = 45

temp = head

while temp:
    if temp.data == key:
        print("Found")
        break
    temp = temp.next
else:
    print("Not Found")