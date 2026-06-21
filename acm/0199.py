from collections import deque

class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(root):
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        n = len(q)
        for i in range(n):
            x = q.popleft()
            if i == n - 1:
                res.append(x.val)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
    return res


root = Node(1, Node(2, Node(5)), Node(3, None, Node(4)))
print(main(root))

root = Node(1, Node(2, Node(4, Node(5))), Node(3))
print(main(root))