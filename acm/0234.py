class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_mid(head):
    p = dummy = Node(next=head)
    q = head
    while q and q.next:
        p = p.next
        q = q.next.next
    return p

def reverse(head):
    p = dummy = Node()
    while head:
        tmp = head.next
        head.next = p.next
        p.next = head
        head = tmp
    return dummy.next

def main(head):
    p = head
    tmp = find_mid(head)
    q = tmp.next
    tmp.next = None
    q = reverse(q)
    while p and q:
        if p.val != q.val:
            return False
        p = p.next
        q = q.next
    return True

head = Node(1, Node(2, Node(2, Node(1))))
print(main(head))

head = Node(1, Node(2))
print(main(head))