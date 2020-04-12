from time import time
start = time()
"""
Since the quadratic must always be positive $\Delta=a^2-4b<0$. Also $b$ must be prime and $a$ odd
"""

def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n < 2:
        return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True


def number_of_primes(x, y):
    n = 0
    if x**2 < 4*y and is_prime(y) and x % 2 != 0:
        while is_prime(n**2+x*n+y):
            n += 1
    else:
        return 0
    return n


N = 1000
list1 = []
list2 = []
list3 = []
for a in range(-N, N+1):
    for b in range(-N, N+1):
        list1.append(number_of_primes(a, b))
        list2.append(a*b)
        list3.append((a, b))
print("The number of primes generated is: " + str(max(list1)))
print("(a,b) is: " + str(list3[list1.index(max(list1))]))
print("a*b is: " + str(list2[list1.index(max(list1))]))
print(time()-start)
