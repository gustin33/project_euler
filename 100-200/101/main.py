from time import time
from math import factorial as fact
start = time()
"""
Using Lagrange´s interpolation formula we obtain that given the first $k$ terms of a sequence $U_1,U_2,...,U_k$
the value of $OP(k,x)$ is given as:

$$ OP(k,x) = \sum_{j=1}^k \frac{U_j(-1)^{k+j}}{(j-1)!(k-j)!} \cdot \prod_{0 \leq h \leq k, h \neq j}(x-h)$$

The sum of all the FIT´s is given by:

$$ S = \sum_{t=1}^k OP(k,k+1)$$
"""


# first we define the sequence u1,u2,...
def h(n):
    return int((n**11+1)/(n+1))


# next we calculate the product (x+1-1)(x+1-2)...(x+1-(j-1))(x+1-(j+1))...(x+1-x)
# which is inside the summation term of OP(x,x+1)
def prod_term(j, x):
    s = 1
    z = 1
    while z < j:
        s = s*(k+1-z)
        z += 1
    if z == j:
        z += 1
        while z <= x:
            s = s*(k+1-z)
            z += 1
    return s


# now we define a function which outputs the FIT OP(x,x+1) for some x
def fit_op(x):
    s = 0
    j = 1
    while j <= x:
        s += int((h(j))*(-1)**(j+x)*prod_term(j, x)/((fact(j-1))*(fact(x-j))))
        j += 1
    return s


# lastly we sum all FIT
lis = []
for k in range(1, 11):
    lis.append(fit_op(k))
print(sum(lis))
print(time()-start)
