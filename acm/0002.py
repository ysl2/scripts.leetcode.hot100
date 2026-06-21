class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main(headA, headB):
    r = dummy = Node()
    p, q = headA, headB
    carry = 0
    while p or q or carry:
        if p:
            carry += p.val
            p = p.next
        if q:
            carry += q.val
            q = q.next
        r.next = Node(val=(carry % 10))
        r = r.next
        carry //= 10
    return dummy.next

headA = Node(2, Node(4, Node(3)))
headB = Node(5, Node(6, Node(4)))

r = main(headA, headB)
print(r.val)
print(r.next.val)
print(r.next.next.val)