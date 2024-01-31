from tree import Node, insert

def sum(root):
    if root is None:
        return 0
    else:
        return root.val + sum(root.left) + sum(root.right)

root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

print(sum(root))
