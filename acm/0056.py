def main(intervals):
    intervals.sort()
    res = []
    for tmp in intervals:
        if res and res[-1][1] >= tmp[0]:
            res[-1][1] = max(res[-1][1], tmp[1])
        else:
            res.append(tmp)
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(main(intervals))