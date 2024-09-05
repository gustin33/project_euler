import math

# Sieve of Eratosthenes to generate prime numbers up to a given limit
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for num in range(2, int(math.sqrt(limit)) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return [x for x, is_prime in enumerate(sieve) if is_prime]

# Function to find the first value that can be written as a sum of primes in over 5000 ways
def find_value(target_ways=5000):
    limit = 10000  # Start with a higher limit
    while True:
        primes = generate_primes(limit)
        ways = [0] * (limit + 1)
        ways[0] = 1  # Base case: 1 way to write 0 as a sum (by taking no primes)
        
        # Use dynamic programming to calculate the number of ways to write each number as the sum of primes
        for prime in primes:
            for i in range(prime, limit + 1):
                ways[i] += ways[i - prime]
        
        # Find the first number with more than the target number of ways
        for i in range(limit + 1):
            if ways[i] > target_ways:
                return i
        
        # If no solution found, increase the limit and try again
        limit *= 2

# Find and print the first number that can be written as a sum of primes in over 5000 ways
result = find_value()
print(result)
