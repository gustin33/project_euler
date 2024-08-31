from time import time
start = time()


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def e_pn(n):
    a, b = 1, 2
    for num in range(2, n+1):
        if num % 3 == 0:
            a, b = b, a + 2*(num//3)*b  # p_3k = 2*k*p_{3k-1} + p_{3k-2}
        else:
            a, b = b, a + b  # then p_k = p_{k-1} + p_{k-2}
    return b


d = 100
while d <= 10**2:
    mid = time()
    print("The {}-th convergent has a numerator whose digital root is {}.".format(d, sum_digits(e_pn(d))))
    print("Time elapsed: {}".format(time()-mid))
    print()
    d *= 10

print("Total time elapsed: {}".format(time()-start))

