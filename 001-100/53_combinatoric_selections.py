from time import time
from math import factorial as f
start = time()
print(sum([1 if f(n)//f(r)//f(n-r) > 10**6 else 0 for n in range(1, 101) for r in range(1, n)]))
print(time()-start)

