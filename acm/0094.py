class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def main(root):
#     if not root:
#         return []
#     return main(root.left) + [root.val] + main(root.right)

def main(root):
    stack = [root]
    res = []
    while stack:
        x = stack.pop()
        if isinstance(x, int):
            res.append(x)
        elif isinstance(x, Node):
            stack += [x.right, x.val, x.left]
    return res

root = Node(1, None, Node(2, Node(3, None, None), None))
print(main(root))