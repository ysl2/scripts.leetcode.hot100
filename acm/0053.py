def main(nums):
    res = nums[0]
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i - 1] + nums[i])
        res = max(res, nums[i])
    return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(main(nums))