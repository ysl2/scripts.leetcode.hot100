def main(nums, k):
    k %= len(nums)
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]

nums = [1,2,3,4,5,6,7]
k = 3
main(nums, k)
print(nums)