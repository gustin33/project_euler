                                                   #108(unfinished)
from functions_list import prime_list_up_to_
from functions_list import is_prime


def number_of_solutions(n):  # returns a list of (prime, valuation)
    if is_prime(n):
        return 2
    if n**0.5 == int(n**0.5):
        if is_prime(int(n**0.5)):
            return 3
    primes = prime_list_up_to_(n)
    num_divisors = 1
    for prime in primes:
        if n % prime == 0:
            h = 1
            while n / (prime**h) == int(n / (prime**h)):  # (1)
                h += 1
            num_divisors = num_divisors*(2*h-1)  # we need to account for the fact that (1) stops being true for
    return (num_divisors + 1)//2  # v+1, where p^v | n , p^{v+1} not | n


n = int(2001**3)
while number_of_solutions(n) <= 1000:
    print(2, n)
    n += 2
print(n)
