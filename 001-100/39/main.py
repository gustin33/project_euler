from collections import Counter
from fractions import gcd
from math import sqrt

def number_pythagorean_triples(t):
    perimeters = []
    for m in range(2, int(sqrt(t / 2))):
        for n in range(1, m):
            if gcd(m, n) == 1 and (m - n) % 2:  # No Duplicates
                for k in range(2 * m * (m + n), t, 2 * m * (m + n)):
                    perimeters.append(k)
    return Counter(perimeters).most_common(1)[0][0]

print(number_pythagorean_triples(1000))
