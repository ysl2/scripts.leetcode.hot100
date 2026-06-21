class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main(head):
    p = q = head
    while q and q.next:
        p = p.next
        q = q.next.next
        if p is q:
            break
    if not (q and q.next):
        return
    p = head
    while p is not q:
        p = p.next
        q = q.next
    return p

tmp = Node(2)
tmp1 = Node(-4)
head = Node(3)
head.next = tmp
head.next.next = Node(0)
head.next.next.next = tmp1
tmp1.next = tmp

print(main(head).val)