def main(n):
    s = '.' * n
    res = []
    def dfs(row, cols, poss, negs, tmp):
        if row == n:
            res.append(tmp)
            return
        for col in range(n):
            if col not in cols and row + col not in poss and row - col not in negs:
                dfs(row + 1, cols | {col}, poss | {row + col}, negs | {row - col}, tmp + [s[:col] + 'Q' + s[col + 1 :]])
    dfs(0, set(), set(), set(), [])
    return res


n = 4
print(main(n))