def main(nums, target):
    nums.sort()
    res = []
    def dfs(nums, tmp):
        if sum(tmp) == target:
            res.append(tmp)
            return
        for i in range(len(nums)):
            if nums[i] > target - sum(tmp):
                break
            dfs(nums[i:], tmp + [nums[i]])
    dfs(nums, [])
    return res


candidates = [2,3,6,7]
target = 7
print(main(candidates, target))