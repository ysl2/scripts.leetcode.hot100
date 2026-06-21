from heapq import heapify, heappop, heappush

class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


def main(lists):
    lists = [l for l in lists if l]
    heapify(lists)
    r = dummy = Node()
    while lists:
        p = heappop(lists)
        r.next = p
        r = r.next
        if p.next:
            heappush(lists, p.next)
    return dummy.next


lists = [Node(1, Node(4, Node(5))),Node(1, Node(3, Node(4))), Node(2, Node(6))]
r = main(lists)

print(r.next.val)
print(r.next.next.val)
print(r.next.next.next.val)
print(r.next.next.next.next.val)
print(r.next.next.next.next.next.val)
print(r.next.next.next.next.next.next.val)
print(r.next.next.next.next.next.next.next.val)
print(r.next.next.next.next.next.next.next.next.val)