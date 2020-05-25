                                                   #643(unfinished)
import math as m
import functions_list as func
from time import time as t
start = t()


def g(n):
    s = 1  # for q = 4, num = 1 (p = 2)
    for q in range(6, n+1, 2):
        if m.log(q, 2) == int(m.log(q, 2)):
            num = q // 2 - 1
        else:
            primes = func.prime_list_up_to_(q)
            num = q // 2
            for prime in primes:
                if q % prime == 0 and prime % 2 != 0:
                    num = num * (prime-1) // prime
        s += num
        if s >= 1000000007:
            s = s % 1000000007
        print(q, s)
    return s


print(g(10**6))
print(t()-start)
45
