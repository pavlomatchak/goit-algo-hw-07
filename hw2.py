from tree import Node, insert

def min_value(root):
    while root.left is not None:
        root = root.left
    return root.val

root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

print(min_value(root))
