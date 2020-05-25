from time import time
start = time()


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def e_pn(n):
    p_n = [1, 2]  # to start we create a list with the first two elements (p_0, p_1)
    num = 2
    while num <= n:  # for all numbers below n
        if num % 3 == 0:  # if 3 | num
            m = num // 3
            p_n.append(2*m*p_n[-1]+p_n[-2])  # p_3k = 2*k*p_{3k-1} + p_{3k-2}
            del p_n[0]  # we delete the first element, so as to keep len(p_n) = 2 and save memory
        else:  # if 3 does not divide num
            p_n.append(p_n[-1]+p_n[-2])  # then p_k = p_{k-1} + p_{k-2}
            del p_n[0]
        num += 1
    return p_n[-1]  # since p_n(list) = [p_{n-1}, p_n](actual numbers), p_n (actual number) = p_n[-1] (list)



d = 100
while d <= 10**4:
    mid = time()
    print("The {}-th convergent has a numerator whose digital root is {}.".format(d, sum_digits(e_pn(d))))
    print("Time elapsed: {}".format(time()-mid))
    print()
    d *= 10

print("Total time elapsed: {}".format(time()-start))

