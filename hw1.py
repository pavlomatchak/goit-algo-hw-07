from tree import Node, insert

def max_value(root):
    while root.right is not None:
        root = root.right
    return root.val

root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

print(max_value(root))
