class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main(head):
    p0 = dummy = Node(next=head)
    p1 = head
    while p1 and p1.next:
        p2 = p1.next
        p3 = p2.next

        p0.next = p2
        p2.next = p1
        p1.next = p3

        p0 = p1
        p1 = p3
    return dummy.next

head = Node(1, Node(2, Node(3, Node(4))))
head = main(head)
print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)