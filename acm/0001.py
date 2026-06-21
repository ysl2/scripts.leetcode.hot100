def main(nums, target):
    mp = {}
    for i, num in enumerate(nums):
        if target - num in mp:
            return [mp[target - num], i]
        mp[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
print(main(nums, target))