file = open("p081_matrix.txt", "r").readlines()
matrix = [line.strip('\n') for line in file]
matrix = [list(map(int, line.split(','))) for line in matrix]

for i in reversed(range(len(matrix))):
    for j in reversed(range(len(matrix[i]))):
        if i + 1 < len(matrix) and j + 1 < len(matrix[i]):
            value = min(matrix[i + 1][j], matrix[i][j + 1])
        elif i + 1 < len(matrix):
            value = matrix[i + 1][j]
        elif j + 1 < len(matrix[i]):
            value = matrix[i][j + 1]
        else:
            value = 0
        matrix[i][j] += value
print(f"min_sum: {matrix[0][0]}")


