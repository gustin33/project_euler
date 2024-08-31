from time import time
import math
start = time()

print('1st solution:')
def power_equal_numb_of_digits(d):
    j = 9
    s = 0
    while j ** d // (10**(d-1)) in range(1, 10):  # 10^(d-1) <= j^d < 10 ^d  ---> 1 <= j/(10^(d-1)) < 10
        s += 1
        j -= 1
    return s


m = 1
S = 0
while power_equal_numb_of_digits(m) != 0:
    S += power_equal_numb_of_digits(m)
    m += 1
print(S)
print(time()-start)

print()
print('2nd solution:')
start = time()
# the maximum n will be such that 9^n < 10 ^ (n-1), i.e.: n = ceil( log_(base = 10/9) (10) )
print(sum([1 if j ** d // (10**(d-1)) in range(1, 10) else 0 for j in range(1, 10)
           for d in range(1, 1+math.ceil(math.log(10, 10/9)))]))
print(time()-start)
