class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


res = 0


def dfs(root):
    global res
    if not root:
        return 0
    l, r = dfs(root.left), dfs(root.right)
    res = max(res, l + r)
    return max(l, r) + 1


def main(root):
    global res
    dfs(root)
    return res


root = Node(1, Node(2, Node(4), Node(5)), Node(3))
print(main(root))