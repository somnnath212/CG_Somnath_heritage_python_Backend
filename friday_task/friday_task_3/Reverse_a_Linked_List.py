class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def reverse(head):
    prev = None
    current = head

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    return prev

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Original:")
print_list(head)

head = reverse(head)

print("Reversed:")
print_list(head)