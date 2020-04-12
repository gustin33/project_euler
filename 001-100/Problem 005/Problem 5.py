from math import gcd

def smallest_multiple(n):
    init = 2
    for num in range(3, n+1):
        init *= num // gcd(init, num)  # we multiple by what init is missing
        # i.e.: say num has a valuation of v on p, then since gcd(num, init)
        # contains all primes that both numbers have in common, we take away
        # the valuation of gcd at p from v.
    return init
print('The smallest multiple up to {} is : {}'.format(10,smallest_multiple(10)))
print('The smallest multiple up to {} is : {}'.format(20,smallest_multiple(20)))
