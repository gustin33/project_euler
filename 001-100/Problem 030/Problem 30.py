from time import time
start = time()


def sum_of_kth_pow_of_n_s_digits(n, k):
    i = 0
    s = 0
    while i < len(str(n)):
        s = s + int(str(n)[i])**k
        i += 1
    return s


j = 2
lis = []
while j < 10**6:
    if sum_of_kth_pow_of_n_s_digits(j, 5) == j:
        lis.append(j)
    j += 1
print(lis)
print(sum(lis))
print(time()-start)
