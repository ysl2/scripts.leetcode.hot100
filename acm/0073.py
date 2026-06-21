def main(matrix):
    row_flag = any(matrix[i][0] == 0 for i in range(len(matrix)))
    col_flag = any(matrix[0][j] == 0 for j in range(len(matrix[0])))

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    if row_flag:
        for i in range(len(matrix)):
            matrix[i][0] = 0
    if col_flag:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
main(matrix)
print(matrix)