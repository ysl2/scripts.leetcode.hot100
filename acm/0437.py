from collections import defaultdict


class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(root, k):
    cnt = defaultdict(int)
    cnt[0] = 1
    pre, res = 0, 0
    def dfs(root):
        nonlocal pre, res
        if not root:
            return
        pre += root.val
        res += cnt[pre - k]
        cnt[pre] += 1
        dfs(root.left)
        dfs(root.right)
        cnt[pre] -= 1
        pre -= root.val
    dfs(root)
    return res