                                                   #50
from time import time as t
from math import factorial as fact
from math import  log as ln
start = t()


# prime test
def is_prime(x):
    isprime = True
    for j in range(2,int(x**0.5)+1):
        if x % j == 0:
            isprime = False
    return isprime


# list of prime numbers p s.t. x <= p <= y
def list_of_primes_xy(x,y):
    primes = []
    a = x
    while (a-5) % 6 != 0:
        a += 1
    for j in range(a,y+1,6):
        if is_prime(j):
            primes.append(j)
    for j in range(a+2,y+1,6):
        if is_prime(j):
            primes.append(j)
    if x <= 3:
        for k in [2,3]:
            primes.append(k)
    primes.sort()
    return primes


# o returns (the prime expressible as a sum of consecutive primes of maximum length, this number being less than x;;its length):
def prime_expressible(x):
    n = 6
    while sum(list_of_primes_xy(2,n)) < x:                               #p_1+...+p_n < upper_bound(n) < x (x = 100 or 10**6)
        n += 1
    n -= 1
    list_primes_xy = list_of_primes_xy(2,n)
    listofprimes = []
    list_of_length_of_sum = []
    for j in range(len(list_primes_xy)):                              #we calculate first s_n=p_1+...+p_n, then s_(n-1),...s_1 = p_1
        if is_prime(sum(list_primes_xy)):
            listofprimes.append(sum(list_primes_xy))
            list_of_length_of_sum.append(len(list_primes_xy))
        list_primes_xy.pop()
    list_primes_xy = list_of_primes_xy(2,n)                                           #list has only one element (p_1 = 2)
    list_primes_xy.reverse()                                          #we change the order of the list
    for j in range(len(list_primes_xy)):                              #we calculate first s_n=p_1+...+p_n, then p_2+...+p_n,...p_n
        if is_prime(sum(list_primes_xy)):
            listofprimes.append(sum(list_primes_xy))
            list_of_length_of_sum.append(len(list_primes_xy))
        list_primes_xy.pop()
    the_max_prime = listofprimes[list_of_length_of_sum.index(max(list_of_length_of_sum))]
    the_length_of_the_chain = max(list_of_length_of_sum)
    return 'The prime is: {}, and its length is: {}'.format(the_max_prime,the_length_of_the_chain)


print(prime_expressible(10**6))
print(t()-start)
