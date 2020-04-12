import itertools
from time import time
from math import gcd
start = time()
b = 9
combinations_a_c = list(itertools.combinations(list(range(10)), 2))
numerator = 1
denominator = 1
print("The four non trivial cases are: ")
for b in range(1, 10):
    for a_c in combinations_a_c:
        a = a_c[0]
        c = a_c[1]
        if (10*a+b)/(10*b+c) == a/c:  # in this case ab / bc = a / c
            print("{}/{} = {}/{} = {}/{}".format(10*a+b, 10*b+c, a, c, a//gcd(a, c), c//gcd(a, c)))
            denominator = denominator * c
            numerator = numerator * a
        if (10*b+a)/(10*c+b) == a/c:  # in this case ba / cb = a / c
            print("{}/{} = {}/{} = {}/{}".format(10 * b + a, 10 * c + b, a, c, a//gcd(a, c), c//gcd(a, c)))
            denominator = denominator * c
            numerator = numerator * a
print("The product of the four fractions is {}/{}.".format(numerator, denominator))
print("The wanted value is {}.".format(denominator//(gcd(denominator, numerator))))
print(time()-start)
