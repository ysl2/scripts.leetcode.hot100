from collections import defaultdict

def main(nums, k):
    cnt = defaultdict(int)
    cnt[0] = 1
    res = 0
    pre = 0
    for num in nums:
        pre += num
        res += cnt[pre - k]
        cnt[pre] += 1
    return res

nums = [1,1,1]
k = 2
print(main(nums, k))