class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(root, p, q):
    if root in (None, p, q):
        return root
    l, r = main(root.left, p, q), main(root.right, p, q)
    if l and r:
        return root
    return l or r