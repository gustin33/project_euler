from time import time
from collections import deque
start = time()

# prime test
def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n < 2:
        return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True


# list prime test
def is_list_prime(x):
    list_is_prime = True
    for j in x:
        if not is_prime(j):
            list_is_prime = False
            break
    return list_is_prime


# returns True if all digits of x are odd and not 5
def all_odd(x):
    propholds = True
    for j in list(map(int, list(str(x)))):
        if j % 2 == 0 or j == 5:
            propholds = False
            break
    return propholds


# primes p below 10^d such that the none of the digits of p is even nor equal to 5 nor divisible by 3 nor 7
def primes_digit(d):
    x = 10**d
    list2 = []
    for num in range(3, x+1, 2):
        if all_odd(num) and is_prime(num):
            list2.append(num)
    return list(set().union(list2, [2, 5]))


# rotations of x
def rotations_of_(x):
    rotations = []
    g = deque(list(str(x)))
    for j in range(len(g)):
        rotations.append(int("".join(list(g))))
        g.rotate(1)
    return rotations


# number of circular primes below 10^d
def circular_primes_below_10__(d):
    s = 0
    for j in primes_digit(d):
        if is_list_prime(rotations_of_(j)):
            s += 1
    return s


print(circular_primes_below_10__(6))
print(time() - start)
