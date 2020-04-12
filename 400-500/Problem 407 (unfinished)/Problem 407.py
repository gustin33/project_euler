                                                   #407(unfinished)
from time import time
from math import gcd
import functions_list as f
start = time()

# prime powers list up to x


def prime_pow_list(x):
    prpow_list = []
    for j in f.prime_list_up_to_(x):
        d = 1
        while j ** d <= x:
            prpow_list.append(j ** d)
            d += 1
    return prpow_list


def m(n):
    lis = [1]
    for a in range(n):
        if a ** 2 % n == a and gcd(a, n) != 1:
            lis.append(a)
    return max(lis)


def sigma_m(n):
    s = len(prime_pow_list(
        n))  # m(1) + m(p_1) + m(p_1^2) + m(p_2) + ... + m(p_j) +...+ m(p_j^m) = 0 + 1 + 1 + ... + 1 = k (p_j^m < N)
    for j in [x for x in range(2, n + 1) if x not in prime_pow_list(
            n)]:  # we start with the first non prime number 4 and analyse all even number up to N
        s += m(j)
    return s


print(sigma_m(10 ** 4))
print(time() - start)

