def main(nums):
    n = len(nums)
    for i in range(n):
        while 0 <= nums[i] - 1 <= n - 1 and nums[nums[i] - 1] != nums[i]:
            tmp = nums[i] - 1
            nums[tmp], nums[i] = nums[i], nums[tmp]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

nums = [1,2,0]
print(main(nums))