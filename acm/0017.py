def main(digits):
    if not digits:
        return []

    mp = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    res = []

    def dfs(nums, tmp):
        if not nums:
            res.append(tmp)
            return
        for c in mp[nums[0]]:
            dfs(nums[1:], tmp + c)
    dfs(digits, '')
    return res


digits = '23'
print(main(digits))