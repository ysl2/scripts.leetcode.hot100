def main(n):
    res = []
    def dfs(remain_open, remain_close, tmp):
        if not remain_open and not remain_close:
            res.append(tmp)
            return
        if remain_open:
            dfs(remain_open - 1, remain_close + 1, tmp + '(')
        if remain_close:
            dfs(remain_open, remain_close - 1, tmp + ')')
    dfs(n, 0, '')
    return res


n = 3
print(main(n))