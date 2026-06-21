def main(grid):
    def dfs(i, j):
        if not (0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[0]) - 1 and grid[i][j] == '1'):
            return
        grid[i][j] = '2'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                res += 1
                dfs(i, j)
    return res


grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
print(main(grid))

grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
print(main(grid))