# def main(grid, target):
#     i, j = 0, len(grid[0]) - 1
#     while i <= len(grid) - 1 and j >= 0:
#         if grid[i][j] == target:
#             return True
#         elif grid[i][j] > target:
#             j -= 1
#         elif grid[i][j] < target:
#             i += 1
#     return False


def main(grid, target):
    m, n = len(grid), len(grid[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        x = grid[mid // n][mid % n]
        if x == target:
            return True
        elif x > target:
            right = mid - 1
        elif x < target:
            left = mid + 1
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(main(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(main(matrix, target))