from time import time
start = time()


def number_of_divisors(n):
    m = n
    divisors = 1  # we use divisors(n) = prod (1+a) where a is the valuation
    if m%2 == 0:
        a = 0
        while m % 2 == 0:
            m = m//2
            a+=1
        divisors*=(a+1)
    prime = 3
    while m != 1:  # of n at p, and the product is over all primes p|n
        if m % prime == 0:
            a = 0
            while m % prime == 0:
                m = m //prime
                a += 1
            divisors *= (a+1)
        prime += 2
    return divisors


def num_div_triangle_number(n, d):
    a, b = d[n], number_of_divisors(n+1)
    d.append(b)
    if n%2==0:
        m = d[n//2]*b
    else:
        m = d[(n+1)//2]*a
    return m


d = [0, 1, 2]
num = 2
divisors = num_div_triangle_number(num, d)
while divisors <=500:
    num += 1
    divisors = num_div_triangle_number(num, d)


print(num*(num+1)//2)
print(time() - start)
