class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, low, high):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)


def main(root):
    return dfs(root, float('-inf'), float('inf'))


root = Node(2, Node(1), Node(3))
print(main(root))
root = Node(5, Node(1), Node(4, Node(3), Node(6)))
print(main(root))