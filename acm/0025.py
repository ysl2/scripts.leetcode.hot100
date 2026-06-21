class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main(head, k):
    p = head
    for _ in range(k):
        if not p:
            return head
        p = p.next
    p = dummy = Node(next=main(p, k))
    for _ in range(k):
        q = head.next
        head.next = p.next
        p.next = head
        head = q
    return dummy.next

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
head = main(head, 3)
print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)
print(head.next.next.next.next.val)