def main(nums):
    n = len(nums)
    res = [1] * n
    for i in range(n - 2, -1, -1):
        res[i] = res[i + 1] * nums[i + 1]
    pre = 1
    for i in range(n):
        res[i] *= pre
        pre *= nums[i]
    return res

nums = [1,2,3,4]
print(main(nums))