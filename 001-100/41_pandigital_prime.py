from eulertools import primes, PermN
from itertools import count

p = primes(int(7654321**.5))
for j in count():
    i = int("".join(PermN("7654321", j)))
    for d in p:
        if i % d == 0:
            break
    else:
        print(i)
