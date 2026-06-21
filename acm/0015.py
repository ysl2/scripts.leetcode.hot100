def main(nums):
    nums.sort()
    n = len(nums)
    res = []
    for first in range(n - 2):
        if first > 0 and nums[first - 1] == nums[first]:
            continue
        third = n - 1
        target = - nums[first]
        for second in range(first + 1, n - 1):
            if second > first + 1 and nums[second - 1] == nums[second]:
                continue
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            if second == third:
                break
            elif nums[second] + nums[third] == target:
                res.append([nums[first], nums[second], nums[third]])
    return res

nums = [-1,0,1,2,-1,-4]
print(main(nums))