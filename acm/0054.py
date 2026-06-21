tmp = ((0, 1), (1, 0), (0, -1), (-1, 0))

def main(matrix):
    m, n = len(matrix), len(matrix[0])
    res = []
    i, j, k = 0, -1, 0
    size = m * n
    while len(res) < size:
        for _ in range(n):
            i += tmp[k][0]
            j += tmp[k][1]
            res.append(matrix[i][j])
        k = (k + 1) % 4
        n, m = m - 1, n
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(main(matrix))