from collections import deque

def main(grid):
    q = deque()
    fresh = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                q.append((i, j, 0))

    res = 0
    while q:
        i, j, t = q.popleft()
        res = max(res, t)
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x <= len(grid) - 1 and 0 <= y <= len(grid[0]) - 1 and grid[x][y] == 1:
                grid[x][y] = 2
                fresh -= 1
                q.append((x, y, t + 1))
    return res if not fresh else -1
