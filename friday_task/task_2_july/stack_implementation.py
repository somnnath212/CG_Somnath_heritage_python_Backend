# stack_implementation.py

class Stack:
    """Stack implementation using Python list."""

    def __init__(self):
        self._data = []     # Internal storage — top = last element

    def push(self, item):
        self._data.append(item)    # append() adds to end (top)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty — cannot pop')
        return self._data.pop()    # pop() removes from end (top)

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty — nothing to peek')
        return self._data[-1]      # Just read the top

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f'Stack (top → bottom): {list(reversed(self._data))}'

# ── Demo ──
s = Stack()
s.push(10); s.push(20); s.push(30)
print(s)
print('Peek:', s.peek())
print('Pop: ', s.pop())
print('After pop:', s)