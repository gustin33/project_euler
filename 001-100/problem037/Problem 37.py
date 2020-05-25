from time import time
start = time()


def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n < 2:
        return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True


def are_all_truncations_prime(number):
    p = str(number)
    truncations = [int(p[:k]) for k in range(1, 1 + len(p))] + [int(p[k:]) for k in range(1, len(p))]
    for truncation in truncations:
        if not is_prime(truncation):
            return False
    return True


j = 1
num = 11
truncatable_primes = []
while j <= 11:
    if is_prime(num) and are_all_truncations_prime(num):
        truncatable_primes.append(num)
        j += 1
    num += 2
print(truncatable_primes)
print(sum(truncatable_primes))
print(time()-start)
