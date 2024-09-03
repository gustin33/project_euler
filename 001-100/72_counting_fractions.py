'''
for each b, the number of reduced fractions 
a/b < 1 
is the number of numbers a < b that are relatively prime to b, which is 
phi(b)
the answer is therefore 
sum(phi(n)) for n=2:10^6'''
def compute_totient_sieve(limit):
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is a prime number
            for j in range(i, limit + 1, i):
                phi[j] *= i - 1
                phi[j] //= i
    return phi


def count_reduced_proper_fractions(n):
    phi = compute_totient_sieve(n)
    return sum(phi[2:])  # Exclude phi[1] since 1 is not a valid denominator


# Set the limit
n = 10**6
total_fractions = count_reduced_proper_fractions(n)

# Print the result
print(
    f"The number of reduced proper fractions for denominators up to {n} is: {total_fractions}"
)
