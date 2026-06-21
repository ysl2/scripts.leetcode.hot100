def main(grid, word):
    def dfs(i, j, k):
        if k == len(word):
            return True
        if not (0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[0]) - 1):
            return False
        if grid[i][j] != word[k]:
            return False
        tmp = grid[i][j]
        grid[i][j] = '#'
        flag = dfs(i - 1, j, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)
        grid[i][j] = tmp
        return flag

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dfs(i, j, 0):
                return True
    return False


board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word = "ABCCED"
print(main(board, word))