from time import time
from math import floor
start = time()
"""
Assuming all odd composite numbers "$n$" can be written in the form $p+2*k^2$ for $p$ prime and some natural number $k$.
We have $0 < p = n-2*k^2$, from where we get that $k$ lies in between $1$ and
$\left \lfloor \sqrt{\frac{n}{2}} \right \rfloor$. Checking with a computer gives the answer fairly fast:
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
n = 9
num = 0
while True:
    flag = 1  # we set a flag to go off once we find the first number not expressible as a sum of a prime and 2*k^2
    if is_prime(n) or is_prime(n-2):  # if n - 2 is prime then n = p + 2 * (1)^2
        n += 2
    else:
        for k in range(1, 1+floor((n/2)**0.5)):
            if is_prime(n-2*k**2):
                flag = 0  # if we fond some k for which n - 2*k^2 is prime, we set the turn off the flag
                break
        if flag:  # everytime we check for the flag
            num += 1
            print("The {}st number is: {}".format(num, n))
            if num == 2:
                break
        n += 2
print(time()-start)
