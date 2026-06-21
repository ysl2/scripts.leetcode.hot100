def main(nums, target):
    def find_min(nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        return left
    def search(nums, left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left <= len(nums) - 1 and nums[left] == target:
            return left
        return -1
    i = find_min(nums)
    if target <= nums[-1]:
        left, right = i, len(nums) - 1
    else:
        left, right = 0, i - 1
    return search(nums, left, right)


nums = [4,5,6,7,0,1,2]
target = 0
print(main(nums, target))

nums = [4,5,6,7,0,1,2]
target = 3
print(main(nums, target))

nums = [1]
target = 0
print(main(nums, target))