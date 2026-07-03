# doubly_linked_list.py

class DNode:
    """Doubly linked list node — has BOTH next and prev pointers."""
    def __init__(self, data):
        self.data = data
        self.next = None   # Pointer to next node
        self.prev = None   # Pointer to previous node

class DoublyLinkedList:
    """
    None ← [5|⇌] ⇌ [10|⇌] ⇌ [20|⇌] ⇌ [30|⇌] → None
           head                           tail
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DNode(data)
        if self.head is None:          # Empty list
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail      # New node's prev = old tail
        self.tail.next = new_node      # Old tail's next = new node
        self.tail = new_node           # Update tail

    def forward(self):
        result = []
        cur = self.head
        while cur:
            result.append(str(cur.data))
            cur = cur.next
        return ' ⇌ '.join(result)

    def backward(self):
        result = []
        cur = self.tail
        while cur:
            result.append(str(cur.data))
            cur = cur.prev
        return ' ⇌ '.join(result)

    def delete(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                if cur.prev: cur.prev.next = cur.next
                else: self.head = cur.next      # Was head
                if cur.next: cur.next.prev = cur.prev
                else: self.tail = cur.prev      # Was tail
                return
            cur = cur.next

dll = DoublyLinkedList()
for val in [10, 20, 30, 40, 50]:
    dll.append(val)
print('Forward: ', dll.forward())
print('Backward:', dll.backward())
dll.delete(30)
print('After deleting 30:',  dll.forward())