from collections import deque


class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(root):
    if not root:
        return []
    queue = deque([root])
    res = []
    while queue:
        tmp = []
        for _ in range(len(queue)):
            x = queue.popleft()
            tmp.append(x.val)
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
        res.append(tmp)
    return res


root = Node(3, Node(9), Node(20, Node(15), Node(7)))
print(main(root))