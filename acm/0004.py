from math import inf


def main(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i

        left1_max = -inf if i == 0 else nums1[i - 1]
        left2_max = -inf if j == 0 else nums2[j - 1]
        left_max = max(left1_max, left2_max)

        right1_min = inf if i == m else nums1[i]
        right2_min = inf if j == n else nums2[j]
        right_min = min(right1_min, right2_min)

        if left_max <= right_min:
            if (m + n) % 2 == 0:
                return (left_max + right_min) / 2
            else:
                return left_max
        elif left1_max > right2_min:
            right = i - 1
        else:
            left = i + 1
    return 0


nums1 = [1,3]
nums2 = [2]
print(main(nums1, nums2))

nums1 = [1,2]
nums2 = [3,4]
print(main(nums1, nums2))