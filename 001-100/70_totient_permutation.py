import time

def compute_totient_sieve(limit):
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is a prime number
            for j in range(i, limit + 1, i):
                phi[j] *= (i - 1)
                phi[j] //= i
    return phi

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def find_min_totient_ratio(limit):
    phi = compute_totient_sieve(limit)
    min_ratio = float('inf')
    result_n = 0
    
    for n in range(2, limit):
        if is_permutation(n, phi[n]):
            ratio = n / phi[n]
            if ratio < min_ratio:
                min_ratio = ratio
                result_n = n
    
    return result_n, min_ratio

# Start timer
start_time = time.time()

# Set the limit to 10^7
limit = 10**7
result_n, min_ratio = find_min_totient_ratio(limit)

# End timer
end_time = time.time()

# Calculate execution time
execution_time = end_time - start_time

# Print the results
print(f"The value of n is: {result_n}")
print(f"The minimum ratio n/phi(n) is: {min_ratio}")
print(f"Execution time: {execution_time:.4f} seconds")
