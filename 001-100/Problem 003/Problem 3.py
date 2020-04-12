from time import time
start = time()
def largest_prime_factor(m):
    n = m
    k = 2
    while k <= n//2:  # largest prime factor will be <= n//2
        if n % k == 0:
            while n % k == 0:
                n = n //k
        k += 1
    return n
    
print(largest_prime_factor(600851475143))
print(time() - start)
