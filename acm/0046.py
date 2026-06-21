def main(nums):
    res = []
    def dfs(nums, tmp):
        nonlocal res
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            dfs(nums[:i] + nums[i + 1 :], tmp + [nums[i]])
    dfs(nums, [])
    return res


nums = [1,2,3]
print(main(nums))