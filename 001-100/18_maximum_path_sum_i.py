from time import time
start = time()
file = open("18_input.txt", "r").read()
matrix = [item.split() for item in file.split("\n")]
grid = [list(map(int, j))for j in matrix]


def maximum_sum(x):
    i = len(x)-1
    while i > 0:
        for j in range(len(x[i]) - 1):
            x[i-1][j] += max([x[i][j], x[i][j+1]])
        x.pop()
        i -= 1
    x = x[0][0]
    return x


print(maximum_sum(grid))
print(time()-start)
