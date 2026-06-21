from collections import deque

class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def main(root):
#     if not root:
#         return 0
#     return max(main(root.left), main(root.right)) + 1


def main(root):
    queue = deque([root])
    res = 0
    while queue:
        res += 1
        for _ in range(len(queue)):
            x = queue.popleft()
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
    return res

root = Node(3, Node(9), Node(20, Node(15), Node(7)))
print(main(root))