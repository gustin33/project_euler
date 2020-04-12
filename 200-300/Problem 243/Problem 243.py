from time import time
from math import ceil
start = time()
"""
This can be solved by hand with a basic hand calculator in some minutes or with a computer in virtually no time.
The resilience $R$ of a number $d$ can be computed as 
$$
R(d) = \frac{\phi (d)}{d-1} =  \frac{d}{d-1} \prod_{p|d} \bigg(1-\frac{1}{p} \bigg)
$$
We require this magnitude to be less than some fraction $\frac{a}{b}$. From 
$$
\frac{d}{d-1} \prod_{p|d} \bigg(1-\frac{1}{p} \bigg) < \frac{a}{b}
$$
we get:
$$
d > \eta \ldots (1), \\
\eta = \frac{\frac{a}{b}}{\frac{a}{b} - \displaystyle \prod_{p|d} \bigg(1-\frac{1}{p} \bigg)}
= \frac{a \prod p}{a\prod p - b \prod (p-1)}
$$
We also ask for $\eta$ to be a nonnull positive integer, this establishes the condition
$$
\frac{a}{b} - \displaystyle \prod_{p|d} \bigg(1-\frac{1}{p} \bigg) > 0 \ldots (2)
$$ 

Using this, together with some additional considerations, we will calculate the searched for value $d$.
For a given fraction $\frac{a}{b}$ we find the least prime number for which $(2)$ is satisfied. After this, and define 
$$
d_1 =  \prod_{p|d} \bigg(1-\frac{1}{p} \bigg), \\ d_n = n d_1 
$$ 
Using (1) for $d_n$ we find $n > \frac{\eta}{d_1}$, from where $n = \left \lceil \frac{\eta}{d_1} \right \rceil$.
And we get the final result as:
$$
d = d_n = n d_1 = \left \lceil \frac{\eta}{d_1} \right \rceil  d_1
$$

So for $a = 15499, \, b = 94744 $ we find that 
$$
\frac{a}{b} - \displaystyle \prod_{p \leq 23} \bigg(1-\frac{1}{p} \bigg) > 0
$$
And 
$$
\eta = 805994497 \, d_1 = 223092870
$$
Hence the number we´re looking for is 
$$
d = d_n = \left \lceil \frac{\eta}{d_1} \right \rceil  d_1 = 892371480
$$

Using a computer is a bit different in the way we calculate the values. To avoid float precision errors $(2)$ becomes:
$$
a \prod p - b \prod (p-1) > 0 \ldots (2^{\prime})
$$
And the looked for number is just 
$$
d = \left \lceil \frac{a}{a\prod p - b\prod(p-1)} \right \rceil \prod p 
$$
Here´s the code: 
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


def least_d_resilience(a, b):  # least d for which R(d) < a/b
    possible_prime = 3
    product_p = 2  # Prod(p); when were done with the while loops product_p = d_1
    product_p_1 = 2-1  # Prod(p-1)
    while True:
        if a * product_p - b * product_p_1 > 0:
            denominator_of_eta = a * product_p - b * product_p_1
            break
        while not is_prime(possible_prime):
            possible_prime += 2
        product_p = product_p * possible_prime
        product_p_1 = product_p_1 * (possible_prime - 1)
        possible_prime += 2
    numerator_of_eta_over_d_1 = a
    d = product_p * ceil(numerator_of_eta_over_d_1 / denominator_of_eta)
    return d


print(least_d_resilience(15499, 94744))
print(time()-start)
