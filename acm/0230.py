class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(root, k):
    res = None
    def dfs(root):
        nonlocal res, k
        if not root or res is not None:
            return
        dfs(root.left)
        if res is not None:
            return
        k -= 1
        if k == 0:
            res = root.val
            return
        dfs(root.right)
    dfs(root)
    return res