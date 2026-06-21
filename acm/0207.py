from collections import defaultdict, deque

def main(n, pres):
    ins = [0] * n
    ads = defaultdict(list)
    for a, b in pres:
        ins[a] += 1
        ads[b].append(a)
    q = deque()
    for i in range(len(ins)):
        if ins[i] == 0:
            q.append(i)
    while q:
        b = q.popleft()
        n -= 1
        for a in ads[b]:
            ins[a] -= 1
            if ins[a] == 0:
                q.append(a)
    return n == 0