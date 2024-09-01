"""
In general if I have an n digit number and I replace k digits from this n, then the 9 generated members will differ by

s = 10^a1+10^a2+...+10^ak

where a1, a2, ..., ak are the indices of the replaced digits, We have

s = 1+ 1 +1 + 1 ... +1  = k (mod3)

If k be 1 or -1 we will have, for the ni generated numbers:
n1     0 mod 3 
n2     1 mod 3
n3     2 mod 3
n4     0 mod 3
n5     1 mod 3
n6     2 mod 3
n7     0 mod 3
n8     1 mod 3
n9     2 mod 3

From this set we only have 6 possible primes, namely
n2
n3
n5
n6
n8
n9

So we need k = 0(3) so that all prime numbers are either 1 or -1 mod 3. 
Now we assume to be looking for a 6 digit number. 
We can either replace 0, 3 or 6 digits. 0 and 6 dont work (6 can be checked manually). so we will have to replace 3 digits
We know also:
1- We will be looking for 6 digit primes with 3 repeated digits (at least)
2- the repeating digit cannot be the last one (since this would mean that we have up to 5 possible primes)
3- We are checking for an eight family, and we are taking the digits from 0-9 so we will only check for primes that have 0, 1 or 2 repeated. Since if they dont have any of these digits repeating we wouldnt have this family


Possible combinations:
n n * * * n
n * n * * n
* n n * * n
n * * n * n
* n * n * n
* * n n * n

n * * * n n
* n * * n n
* * n * n n

* * * n n n
"""

import sympy as sp
import re

sieve = list(sp.sieve.primerange(10**5, 10**6))


def filter_numbers_with_three_repeated_digits(numbers):
    filtered_numbers = []

    for number in numbers:
        number_str = str(number)
        # Check if any digit occurs 3 or more times
        if any(number_str.count(digit) >= 3 for digit in "0123456789"):
            filtered_numbers.append(number)
    print(f"Filtered out {len(numbers) - len(filtered_numbers)}")
    print(f"Remaining {len(filtered_numbers)}")
    return filtered_numbers


# Example usage
sieve = filter_numbers_with_three_repeated_digits(sieve)

possible_regex = [
    r"\d\d(\d)\1\1\d",
    r"\d(\d)\d\1\1\d",
    r"(\d)\d\d\1\1\d",
    r"\d(\d)\1\d\1\d",
    r"(\d)\d\1\d\1\d",
    r"(\d)\1\d\d\1\d",
    r"\d(\d)\1\1\d\d",
    r"(\d)\d\1\1\d\d",
    r"(\d)\1\d\1\d\d",
    r"(\d)\1\1\d\d\d",
]

def find_prime():
    minimum_prime = 10**6
    # Divide the sieve into lists with same remainder mod 3
    for prime in sieve:
        for pattern in possible_regex:
            regex = re.compile(pattern)
            if regex.match(str(prime)):
                base_pattern = str(prime)
                pattern_to_replace = pattern.replace(r"(\d)", "*")
                pattern_to_replace = pattern_to_replace.replace(r"\1", "*")
                pattern_to_replace = pattern_to_replace.replace(r"\d", "n")
                for i, digit in enumerate(str(prime)):
                    if pattern_to_replace[i] == "*":
                        base_pattern = base_pattern[:i] + "*" + base_pattern[i+1:]
                base_pattern = base_pattern.replace("*", r"(\1)")
                base_pattern = base_pattern.replace(r"(\1)", r"(\d)", 1)
                base_pattern = re.compile(base_pattern)

                matches = [prime for prime in sieve if base_pattern.match(str(prime))]
                if len(matches) >= 8:
                    print(matches)
                    
                    return min(matches)


print(f"Answer: {find_prime()}")
# for i in range(1, 3):
#     same_remainder_sieve = [prime for prime in sieve if prime % 3 == i]
#     for pattern in possible_combinations:
#         for i in range(10):
#             pattern = pattern.replace("*", f"{i}")
#             pattern = pattern.replace("n", "\d")

#             regex = re.compile(pattern)
#             same_pattern = [
#                 prime for prime in same_remainder_sieve if regex.match(str(prime))
#             ]
#             new_min_prime = min(same_pattern)
#             print(same_pattern)
#             break
#             if len(same_pattern) >= 8 and new_min_prime < minimum_prime:
#                 minimum_prime = new_min_prime
#         break
#     break

# print(f"Answer: {minimum_prime}")
