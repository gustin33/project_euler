def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, limit + 1):
        if sieve[i]:
            primes.append(i)
            for multiple in range(i * i, limit + 1, i):
                sieve[multiple] = False
    return primes

def count_prime_sums(limit, primes):
    ways = [0] * (limit + 1)
    ways[0] = 1  # There's one way to make 0 (no primes)

    for prime in primes:
        for i in range(prime, limit + 1):
            ways[i] += ways[i - prime]

    return ways

def find_first_value(threshold):
    limit = 10000  # Starting with a reasonable upper bound
    primes = sieve_of_eratosthenes(limit)

    while True:
        ways = count_prime_sums(limit, primes)
        for i in range(len(ways)):
            if ways[i] > threshold:
                return i
        # Increase the limit and search again
        limit *= 2
        primes = sieve_of_eratosthenes(limit)

if __name__ == "__main__":
    result = find_first_value(5000)
    print("The first value which can be written as the sum of primes in over 5000 different ways is:", result)
