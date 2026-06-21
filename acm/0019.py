class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main(head, n):
    p = dummy = Node(next=head)
    for _ in range(n):
        p = p.next
    q = dummy
    while p.next:
        p = p.next
        q = q.next
    q.next = q.next.next
    return dummy.next

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
main(head, 2)
print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)