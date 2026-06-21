def main(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(len(matrix)):
        matrix[i].reverse()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
main(matrix)
print(matrix)