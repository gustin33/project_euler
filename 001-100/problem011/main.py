from time import time
from operator import mul
from functools import reduce
start = time()
f = open('p011_grid.txt', 'r').read()
matrix = [item.split() for item in f.split("\n")]
list1 = [list(map(int, j)) for j in matrix]


# maximum product of d integers on x(2-d array)
def max_prod(x, d):
    list0 = []
    for row in x:  # x is a list of lists, each element of x is the row of the matrix
        list0.append(max([reduce(mul, y, 1) for y in [row[i - d:i] for i in range(d, 1 + len(x))]]))
    for column in [[row[i] for row in x] for i in range(len(x))]:  # the list consisting of the i-th element
        # of each list(row) of x is a column of the matrix
        list0.append(max([reduce(mul, y, 1) for y in [column[i - d:i] for i in range(d, 1 + len(x))]]))
    principal_diagonals = [[x[i+j][i] for i in range(len(x)-j)] for j in range(len(x)+1-d)] +\
                          [[x[i][i+j] for i in range(len(x)-j)] for j in range(1, len(x)+1-d)]
    for diagonal in principal_diagonals:
        list0.append(max([reduce(mul, y, 1) for y in [diagonal[i - d:i] for i in range(d, 1 + len(x))]]))
    non_princ_diagonals = [[x[i][len(x) - i - 1 - j] for i in range(len(x) - j)] for j in range(len(x) + 1 - d)] + [
        [x[len(x) - 1 - i][i + j] for i in range(len(x) - j)] for j in range(1, len(x) + 1 - d)]
    for diagonal in non_princ_diagonals:
        list0.append(max([reduce(mul, y, 1) for y in [diagonal[i - d:i] for i in range(d, 1 + len(x))]]))
    return max(list0)


print(max_prod(list1, 4))
print(time()-start)
