# traversals.py

def inorder(node, result=None):
    """Left → Node → Right"""
    if result is None: result = []
    if node:
        inorder(node.left, result)    # 1. Go left
        result.append(node.data)      # 2. Visit node
        inorder(node.right, result)   # 3. Go right
    return result

def preorder(node, result=None):
    """Node → Left → Right"""
    if result is None: result = []
    if node:
        result.append(node.data)       # 1. Visit node FIRST
        preorder(node.left, result)    # 2. Go left
        preorder(node.right, result)   # 3. Go right
    return result

def postorder(node, result=None):
    """Left → Right → Node"""
    if result is None: result = []
    if node:
        postorder(node.left, result)   # 1. Go left
        postorder(node.right, result)  # 2. Go right
        result.append(node.data)       # 3. Visit node LAST
    return result

def level_order(root):
    """BFS — visit level by level (left to right)."""
    from collections import deque
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    return result

print('Inorder:    ', inorder(root))
print('Preorder:   ', preorder(root))
print('Postorder:  ', postorder(root))
print('Level Order:', level_order(root))