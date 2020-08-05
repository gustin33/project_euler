from time import time
from itertools import permutations
start = time()
lis = list(permutations(list(str(9876543210))))
lis.sort()
print("".join(lis[10**6-1]))
print(time()-start)

