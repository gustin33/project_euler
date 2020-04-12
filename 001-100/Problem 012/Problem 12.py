from time import time
start = time()


def number_of_divisors(n):
    prime = 2
    m = n
    divisors = 1  # we use divisors(n) = prod (1+a) where a is the valuation
    while m != 1:  # of n at p, and the product is over all primes p|n
        if m % prime == 0:
            a = 0
            while m % prime == 0:
                m = m //prime
                a += 1
            divisors *= a+1
        prime += 1
    return divisors


def triangle_number(n):
    return n*(n+1) //2


num = 1
while number_of_divisors(triangle_number(num)) <=500:
    num += 1


print(triangle_number(num))
print(time() - start)
