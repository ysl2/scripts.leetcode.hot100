def main(height):
    left, right = 0, len(height) - 1
    res = 0
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        res = max(res, h * w)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return res

height = [1,8,6,2,5,4,8,3,7]
print(main(height))