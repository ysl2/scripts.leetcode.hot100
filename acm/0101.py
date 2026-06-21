class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(p, q):
    if not (p and q):
        return p is q
    return p.val == q.val and dfs(p.left, q.right) and dfs(p.right, q.left)


def main(root):
    return not root or dfs(root.left, root.right)


root = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))
print(main(root))