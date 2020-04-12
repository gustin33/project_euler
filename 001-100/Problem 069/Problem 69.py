from time import time

start = time()
"""
Since phi(n)= n* Prod(1-1/p), n/phi(n) = Prod(1-1/p)^-1  will be a maximum when the amount of prime numbers "p"
under the product "Prod" is maximum. I.e. for n < N, the looked for number is a = p_1*p_2*...p_k, with a < N

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


def totient_maximum(x):
    j = 2
    product = 1
    while product < x:
        if is_prime(j):
            product = product * j
        j += 1
    return product // (j-1)   # we remove the last element which makes the product > 100


d = 6
while d < 100000:
    start = time()
    print("For n less than 10^ " + str(d) + ", the number that produces the maximum m/phi(m) is " +
          str(totient_maximum(10**d)))
    print(". Time elapsed: " + str(time()-start))
    d += 10000
print(time()-start)
