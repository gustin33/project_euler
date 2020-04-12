                                                   #347(unfinished)
from time import time
from functions_list import prime_nth
from functions_list import prime_list_up_to_
start = time()


def m(p, q, n):
    j = 0
    while True:
        x = n - j
        y = x
        if x % p == 0:
            while x % p == 0:
                x = x//p
            if x % q == 0:
                while x % q == 0:
                    x = x//q
                if x == 1:
                    return y
                else:
                    x = n-j
            else:
                x = n - j
        elif x % q == 0:
            while x % q == 0:
                x = x//q
            if x % p == 0:
                while x % p == 0:
                    x = x//p
                if x == 1:
                    return y
                else:
                    x = n-j
            else:
                x = n - j
        if x == 1:
            return 0
        j += 1


def s(n):
    summation = 0
    x = 1
    while prime_nth(x)*prime_nth(x+1) <= n:
        x += 1
    x -= 1
    print(x)
    for p in prime_list_up_to_(1+prime_nth(x)):
        for q in prime_list_up_to_(n//p):
            if q > p:
                summation += m(p, q, n)
                print((p, q), m(p, q, n))
    return summation


print(s(10000))
print(time()-start)
