class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main(headA, headB):
    r = dummy = Node()
    p, q = headA, headB
    while p and q:
        if p.val <= q.val:
            r.next = p
            r = r.next
            p = p.next
        else:
            r.next = q
            r = r.next
            q = q.next
    r.next = p or q
    return dummy.next

headA = Node(1)
headA.next = Node(2)
headA.next.next = Node(4)

headB = Node(1)
headB.next = Node(3)
headB.next.next = Node(4)

r = main(headA, headB)
print(r.val)
print(r.next.val)
print(r.next.next.val)
print(r.next.next.next.val)
print(r.next.next.next.next.val)