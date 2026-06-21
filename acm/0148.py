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

def merge_two(p, q):
    r = dummy = Node()
    while p and q:
        if p.val <= q.val:
            tmp = p.next
            r.next = p
            r = r.next
            p = tmp
        else:
            tmp = q.next
            r.next = q
            r = r.next
            q = tmp
    r.next = p or q
    return dummy.next

def main(head):
    if not (head and head.next):
        return head
    tmp = find_mid(head)
    head1 = tmp.next
    tmp.next = None
    head, head1 = main(head), main(head1)
    return merge_two(head, head1)

head = Node(4, Node(2, Node(1, Node(3))))
head = main(head)
print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)