                                                   #81 (unfinished)
import numpy as np
input = np.loadtxt("p081_matrix.txt", dtype='i', delimiter=',')
def path_sum(matrix):
    n = len(matrix)
    i, j = n-1, n-1
    s = matrix[i][j]
    while j > 0 and i >= 0 or i > 0 and j >= 0:
        if matrix[i][j-1] < matrix[i-1][j]:
            s += matrix[i][j-1]
            j -= 1
        else:
            s += matrix[i-1][j]
            i -= 1
    return s


x = [319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]
print("the passcode is {} , of length {}".format(f(x),len(f(x))))
