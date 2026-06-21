class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(nums):
    return nums and Node(nums[m := len(nums) // 2], main(nums[:m]), main(nums[m + 1:]))


nums = [-10, -3, 0, 5, 9]
root = main(nums)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.right.left.val)