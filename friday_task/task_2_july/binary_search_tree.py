# binary_search_tree.py

class BSTNode:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # ── INSERT ────────────────────────────────────────────────
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:          # Found empty spot — insert here
            return BSTNode(data)
        if data < node.data:
            node.left  = self._insert(node.left,  data)  # Go left
        elif data > node.data:
            node.right = self._insert(node.right, data)  # Go right
        # If data == node.data: skip (no duplicates in BST)
        return node

    # ── SEARCH ────────────────────────────────────────────────
    def search(self, data):
        return self._search(self.root, data, depth=0)

    def _search(self, node, data, depth):
        if node is None:
            return None, depth   # Not found
        if data == node.data:
            return node, depth   # Found!
        elif data < node.data:
            return self._search(node.left,  data, depth+1)
        else:
            return self._search(node.right, data, depth+1)

    # ── DELETE ────────────────────────────────────────────────
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None: return None

        if data < node.data:         # Go left
            node.left  = self._delete(node.left,  data)
        elif data > node.data:       # Go right
            node.right = self._delete(node.right, data)
        else:                        # Found the node to delete!
            # Case 1: Leaf node (no children)
            if not node.left and not node.right:
                return None
            # Case 2: One child
            if not node.left:  return node.right
            if not node.right: return node.left
            # Case 3: Two children
            # Find inorder successor (smallest in right subtree)
            successor = self._min_node(node.right)
            node.data  = successor.data     # Copy successor's data
            node.right = self._delete(node.right, successor.data)
        return node

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    # ── TRAVERSALS ────────────────────────────────────────────
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)

    def display(self):
        print('BST Inorder (sorted):', self.inorder())

# ── Demo ──
bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

bst.display()

node, depth = bst.search(60)
print(f'Search 60: Found={node is not None}, Depth={depth}')
node, depth = bst.search(99)
print(f'Search 99: Found={node is not None}')

bst.delete(30)  # Delete node with 2 children
print('After deleting 30:', bst.inorder())