def summation_of_primes(n):
    primes = [2]
    num = 3
    while num < n:
        print(num)
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 2
    return sum(primes)

print(summation_of_primes(10))
print(summation_of_primes(2*10**6))
