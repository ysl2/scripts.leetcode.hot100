class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(root):
    if not root:
        return []
    main(root.left)
    main(root.right)
    tmp = root.right
    root.right = root.left
    root.left = None
    p = root
    while p and p.next:
        p = p.next
    p.next = tmp