def main(nums, target):
    def bisect_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return left
    l, r = bisect_left(nums, target), bisect_left(nums, target + 1) - 1
    return [l, r] if l <= r else [-1, -1]


nums = [5,7,7,8,8,10]
target = 8
print(main(nums, target))

nums = [5,7,7,8,8,10]
target = 6
print(main(nums, target))

nums = []
target = 0
print(main(nums, target))