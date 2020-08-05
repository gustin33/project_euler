from time import time
start = time()
m = 10**6
print(sum([j if list(str(j))[::-1] == list(str(j)) and list("{0:b}".format(j))[::-1] == list("{0:b}".format(j))
           else 0 for j in range(1, m+1, 2)]))
print(time()-start)
start = time()


def double_base_sum(n):
    s = 0
    for j in range(1, n+1, 2):
        if list(str(j))[::-1] == list(str(j)) and list("{0:b}".format(j))[::-1] == list("{0:b}".format(j)):
            s += j
    return s


print(double_base_sum(m))
print(time()-start)
