class Node():
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def main(head):
    if not head:
        return
    mp = {}
    p = head
    while p:
        mp[p] = Node(p.val)
        p = p.next
    for k in mp:
        mp[k].next = mp.get(k.next)
        mp[k].random = mp.get(k.random)   
    return mp.get(head)

node0 = Node(7)
node1 = Node(13)
node2 = Node(11)
node3 = Node(10)
node4 = Node(1)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

node0.random = None
node1.random = node0
node2.random = node4
node3.random = node2
node4.random = node0

r = main(node0)

print(r.val)
print(r.next.val)
print(r.next.next.val)
print(r.next.next.next.val)
print(r.next.next.next.next.val)
print()
print(r.next.random.val)
print(r.next.next.random.val)
print(r.next.next.next.random.val)
print(r.next.next.next.next.random.val)