import sympy

# Limit
limit = 50_000_000

# Step 1: Generate primes up to appropriate limits for squares, cubes, and fourth powers
primes_for_squares = list(sympy.primerange(2, int(limit**0.5) + 1))  # up to sqrt(limit)
primes_for_cubes = list(sympy.primerange(2, int(limit**(1/3)) + 1))  # up to cbrt(limit)
primes_for_fourths = list(sympy.primerange(2, int(limit**0.25) + 1))  # up to fourth root of limit

# Step 2: Generate all prime squares, cubes, and fourth powers below the limit
prime_squares = [p**2 for p in primes_for_squares]
prime_cubes = [p**3 for p in primes_for_cubes]
prime_fourths = [p**4 for p in primes_for_fourths]

# Step 3: Calculate sums of prime square, cube, and fourth power and store unique values
unique_sums = set()

# Milestones for progress reporting
milestones = [50, 500, 5000, 50000, 500000, 5000000, 50_000_000]

for square in prime_squares:
    if square >= limit:
        break  # Early exit if square already exceeds limit
    for cube in prime_cubes:
        if square + cube >= limit:
            break  # Early exit if square + cube exceeds limit
        for fourth in prime_fourths:
            total_sum = square + cube + fourth
            if total_sum >= limit:
                break  # Early exit if total_sum exceeds limit
            unique_sums.add(total_sum)

            # Check if we hit a milestone
            if len(unique_sums) in milestones:
                print(f"Reached {len(unique_sums)} unique sums")

# Step 4: Final count of unique sums
print(f"Total unique sums: {len(unique_sums)}")
