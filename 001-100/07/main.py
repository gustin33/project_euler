def nth_prime(n):
    primes = [2]
    number = 3
    counter = 1
    while counter < n:
        if not(any(number % prime == 0 for prime in primes)):
            primes.append(number)
            counter += 1
        number += 2
    return primes[-1]

# print('The {}-th prime is: {}'.format(6,nth_prime(6)))
print('The {}-th prime is: {}'.format(10001,nth_prime(10001)))

