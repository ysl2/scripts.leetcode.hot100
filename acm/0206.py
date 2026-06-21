class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def main(head):
    p = dummy = Node(0)
    while head:
        tmp = head.next
        head.next = p.next
        p.next = head
        head = tmp
    return dummy.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

head = main(head)
print(head.val, head.next.val, head.next.next.val)