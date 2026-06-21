def main(height):
    left, right = 0, len(height) - 1
    ml, mr = 0, 0
    res = 0
    while left < right:
        ml = max(ml, height[left])
        mr = max(mr, height[right])
        if height[left] <= height[right]:
            res += ml - height[left]
            left += 1
        else:
            res += mr - height[right]
            right -= 1
    return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(main(height))