                                                   #346(unfinished)
from time import time
import math as m
start = time()
s = 1  # 1 is a strong repunit in every base
for x in range(7, 10**2):
    for b in range(2, 1 + m.floor(((4*x-3)**0.5-1)/2)):
        n = round(m.log(1+(b-1)*x, b), 5)  # we round the number up to the fifth decimal because of imprecision
        # when dealing with float calculations
        print(x, b)
        if n == int(n):
            s += x
            break
print(s)
print(time()-start)
