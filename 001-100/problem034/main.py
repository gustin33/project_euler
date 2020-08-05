from time import time
import math

start = time()
"""
The upper bound $9 999 999$ is a bit much,
Firstly, note that it is not possible for a number like $999...$ with "$N$" $9$´s to follow the property, since:

$$9999...=9*111...=9*odd=9!+9!+9!+...=N*9!=9*even$$

So at least 1 digit is less than 9. Taking $z=abcd...$ to have $m$ digits we have:

$$a,bc..*10^{m-1}=abc...=a!+b!+c!+... \leq 8!+9!+9!+...=8!+(m-1)*9!$$
In other words:
$$a,bc...*10^{m-1} \leq (9m-8)*8! \, \ldots \, (1)$$

Where the numbers after the comma represent the decimal part of the number. For $m=8$ you have:

$$a,bc...*10^7 < 2,59*10^6$$

Which is not possible. From now on everytime you add $1$ to $m$ you will \
add to the LHS a number bigger than $9*(a,bc...*10^7)>9*10^7$ (since you´re \
multiplying $z$ by $10$, the difference being $9*z$). But on the RHS you´ll just keep \
adding, at most, $9!=362 880 <3,63*10^5$. It follows that for $m \geq 8$ LHS of (1) is bigger than RHS.
Hence take $m \leq 7$.
When $m=7$, the upper bound is $(9*7-8)*8!=2 217 600$. I took this number as an upper bound.
The code i´ve used (in python) is:
"""


def sum_of_fact_of_digits(n):
    i = 0
    value_of_sum = 0
    while i < len(str(n)):
        value_of_sum = value_of_sum + math.factorial(int(str(n)[i]))
        i += 1
    return value_of_sum


j = 3
s = 0
while j < 2217600:
    j += 1
    if sum_of_fact_of_digits(j) == j:
        s += j
        print(j)
print(s)
print(time() - start)
