import time

def factors(n, memo):
    if n in memo:
        return memo[n]
    
    result = []
    limit = int(n ** 0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            # i is a factor, and so is n // i
            result.append(sorted([i, n // i]))
            # Recursively find factors of i and n // i
            for factor_list in factors(i, memo):
                result.append(sorted([n // i] + factor_list))
            for factor_list in factors(n // i, memo):
                result.append(sorted([i] + factor_list))
    
    memo[n] = result
    return result

# Start timer
start_time = time.time()

# Initialize memoization dictionary
memo = {}

# Initialize results array
results = [0] * 12001

for i in range(4, 13001):
    for factor_list in factors(i, memo):
        result = len(factor_list) + i - sum(factor_list)
        if result < 12001 and results[result] == 0:
            results[result] = i

# Generate the final result
unique_results = set(results)
total_sum = sum(unique_results)

# End timer
end_time = time.time()
elapsed_time = end_time - start_time

# Print results
print("Unique results for the given conditions:")
print(f"Count of unique results: {len(unique_results)}")
print(f"Sum of unique results: {total_sum}")
print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Optionally, print the actual results if needed
# print("Unique results:", sorted(unique_results))
