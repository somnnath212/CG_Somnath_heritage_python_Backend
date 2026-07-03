class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

def min_value(node):
    while node.left:
        node = node.left
    return node

def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)

    elif key > root.key:
        root.right = delete(root.right, key)

    else:
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        temp = min_value(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

values = [40, 20, 60, 10, 30, 50, 70]

root = None
for i in values:
    root = insert(root, i)

root = delete(root, 20)

print("Inorder:")
inorder(root)