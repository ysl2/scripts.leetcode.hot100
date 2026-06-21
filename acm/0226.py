class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(root):
    if not root:
        return
    root.left, root.right = main(root.right), main(root.left)
    return root


root = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
root = main(root)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.left.right.val)
print(root.right.left.val)
print(root.right.right.val)