from time import time
start = time()

def sum_of_multiples(n,p,q):  # calculates sum of all multiples of p and q under n
    multiples_of_p = set(range(0, n, p))
    multiples_of_q = set(range(0, n, q))
    return sum(multiples_of_p.union(multiples_of_q))

print(sum_of_multiples(1000, 3, 5))
print(time()-start)
