class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(preorder, inorder):
    mp = {v: k for k, v in enumerate(inorder)}
    def dfs(root, left, right):
        if left > right:
            return
        i = mp[preorder[root]]
        return Node(preorder[root], dfs(root + 1, left, i - 1), dfs(i - left + 1 + root, i + 1, right))
    return dfs(0, 0, len(inorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = main(preorder, inorder)
print(root.val)
print(root.left.val, root.right.val)
print(root.right.left.val, root.right.right.val)
