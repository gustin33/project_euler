from time import time
from functools import reduce
from operator import mul
start = time()
"""
If one takes the numbers $1$ to $x$ and concatenates them like so:
$$1234567891011...$$
The length of this integer is $$S =\sum_1^n 9j*10^{j-1}+(n+1)(x-10^n+1)$$

Where $n=\left \lfloor{\log_{10} x}\right \rfloor$ (i.e. $10^n \leq x < 10^{n+1}$) .
We require this sum to be at least $10^6$. So for $n = 5$, and taking $S \geq 10^6$.
We get $x \geq 185186$, with a length of $S \geq 1000005$.
"""
n = 185186
list1 =list(
            map(
                int, list(
                    ''.join(
                        list(map(str, list(range(1, n))))
                            )
                        )
                )
            )
print(reduce(mul, [list1[10**j-1] for j in range(7)]))
print(time()-start)
