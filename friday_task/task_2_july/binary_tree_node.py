# binary_tree_node.py

class TreeNode:
    def __init__(self, data):
        self.data  = data
        self.left  = None   # Left child
        self.right = None   # Right child

# Build the tree shown above manually
root = TreeNode(1)
root.left  = TreeNode(2)
root.right = TreeNode(3)
root.left.left   = TreeNode(4)
root.left.right  = TreeNode(5)
root.right.left  = TreeNode(6)
root.right.right = TreeNode(7)

def height(node):
    """Calculate the height of a binary tree recursively."""
    if node is None:    # Empty tree has height 0
        return 0
    left_h  = height(node.left)
    right_h = height(node.right)
    return 1 + max(left_h, right_h)  # 1 (this node) + tallest subtree

def count_nodes(node):
    if node is None: return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def count_leaves(node):
    if node is None: return 0
    if node.left is None and node.right is None: return 1  # Leaf!
    return count_leaves(node.left) + count_leaves(node.right)

print('Height:',      height(root))
print('Total nodes:', count_nodes(root))
print('Leaf nodes:',  count_leaves(root))