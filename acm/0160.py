class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def main(headA, headB):
    pA, pB = headA, headB
    while pA is not pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA

tmp = Node(8)
tmp.next = Node(4)
tmp.next.next = Node(5)

headA = Node(4)
headA.next = Node(1)
headA.next.next = tmp

headB = Node(5)
headB.next = Node(6)
headB.next.next = Node(1)
headB.next.next.next = tmp

print(main(headA, headB).val)