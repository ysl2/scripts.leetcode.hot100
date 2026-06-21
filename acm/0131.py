def main(s):
    res = []
    def dfs(s, tmp):
        nonlocal res
        if not s:
            res.append(tmp)
            return
        for i in range(len(s)):
            t = s[: i + 1]
            if t == t[::-1]:
                dfs(s[i + 1 :], tmp + [t])
    dfs(s, [])
    return res


s = "aab"
print(main(s))