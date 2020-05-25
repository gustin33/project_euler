from time import time as t
from functions_list import prime_list_up_to_
from functions_list import euler_totient as phi
import itertools
start = t()


def is_a_permutation_of_b(a, b):
    return set(str(a)).intersection(set(str(b))) == set(str(a))


def f(m):
    # the numbers which have the least ratio m/phi(m) have only two prime divisors
    n = 3
    while prime_list_up_to_(n)[-1] * prime_list_up_to_(n)[-2] < m:  # we form a list of prime numbers, such that----(1)
        n += 1  # the last two elements´ product is less than some given quantity "N", say N = 100
    n -= 1  # we subtract one since the last n does not satisfy "(1)"
    a = list(itertools.combinations(prime_list_up_to_(n), 2))  # we perform a combination of 2 out of the prime list
    b = [j[0] * j[1] for j in a if is_a_permutation_of_b(j[0]*j[1], phi(j[0]*j[1]))]  # # we form a new list made of the
    # product of each tuple, if phi(element) is a permutation of element
    b.sort()  # we rearrange the list
    j, number, ratio = 0, 6, 6/phi(6)  # 6 = 2*3
    while j < len(b):
        u = b[j]  # we begin with the first element of b
        if u / phi(u) < ratio:  # if the ratio is less than the number before in b
            number = u  # change the value of "number" to this element
            ratio = u/phi(u)  # do the same with ratio
        j += 1
    return "The searched for number is {}. And the ratio is {}".format(number, ratio)


print(f(10**5))
print(t()-start)
