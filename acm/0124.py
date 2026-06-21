class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(root):
    res = float('-inf')
    def dfs(root):
        nonlocal res
        if not root:
            return 0
        l, r = dfs(root.left), dfs(root.right)
        res = max(res, l + r + root.val)
        return max(max(l, r) + root.val, 0)
    dfs(root)
    return res