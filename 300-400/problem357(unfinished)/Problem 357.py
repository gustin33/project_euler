                                                   #357(unfinished)
import functions_list as f
from time import time as t
from functools import reduce

start = t()


def sum_numbers_less_than(n):  # g returns true if the property holds:
    possible_numbers = [1, 2]  # for 2 prop holds
    for num in range(1, n//2 + 1, 2):  # if num is odd, all its divisors are too and num/div+div
        # is even and not prime for num not 1. also num/2 is odd
        num = num*2
        if reduce(lambda x, y: x * y, f.prime_divisors_of(num)) == num and f.is_prime(num + 1) and \
                not (f.is_prime(num)):
            possible_numbers.append(num)
    # 1)Numbers for which prop holds are products of primes.
    # 2)Since all numbers will have 1 as a divisor, 1+n/1 = n+1 must be prime.
    # 3)If n is prime, the only divisors are 1 and d, but then taking 1 as a divisor:
    # 4)divisor + number/divisor = 1+n/1=n+1=even number
    for num in possible_numbers:
        prop_holds = True  # we assume the prop holds until we check all divisors of n,
        # or we find one divisor for which the prop does not hold
        for divisor in f.divisors_of(num):
            if not (f.is_prime(divisor + num // divisor)):
                prop_holds = False
                break
        if not prop_holds:
            possible_numbers.remove(num)
    return possible_numbers
print([num for num in sum_numbers_less_than(1000)])
