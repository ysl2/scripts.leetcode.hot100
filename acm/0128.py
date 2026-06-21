def main(nums):
    nums = set(nums)
    res = 0
    for num in nums:
        if num - 1 in nums:
            continue
        tmp = 1
        while num + 1 in nums:
            tmp += 1
            num += 1
        res = max(res, tmp)
    return res

nums = [100,4,200,1,3,2]
print(main(nums))