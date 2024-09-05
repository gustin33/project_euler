from collections import defaultdict
import math


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
 

def generate_pythagorean_triples(limit):
    perimeters = defaultdict(int)

    # Generate Pythagorean triples using the formula
    for m in range(2, int(math.sqrt(limit / 2)) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                perimeter = a + b + c
                print(a, b, c )
                while perimeter <= limit:
                    perimeters[perimeter] += 1
                    perimeter += a + b + c  # all other pythagorean triples are multiples of the primitive ones
    return perimeters


def count_unique_perimeters(limit):
    perimeters = generate_pythagorean_triples(limit)
    return sum(1 for count in perimeters.values() if count == 1)


if __name__ == "__main__":
    limit = 120# 1500000
    result = count_unique_perimeters(limit)
    print(
        f"The number of lengths that can form exactly one integer-sided right-angled triangle is: {result}"
    )
