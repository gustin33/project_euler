import itertools
from time import time
start = time()
def sum_square_difference(n):
    s = 0
    for a, b in itertools.combinations(range(1,n+1),2):
        s += 2*a*b
    return s

print('For n = {}: {}'.format(10, sum_square_difference(10)))
print('For n = {}: {}'.format(100, sum_square_difference(100)))

print(time()-start)
