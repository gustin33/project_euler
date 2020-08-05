from time import time
start = time()


def first_fib_num_to_have_x_digits(x):
    n = 2
    flist = [1, 1]
    while flist[-1] < 10**(x-1):
        flist.append(flist[0] + flist[1])
        del flist[0]
        n += 1
    return "F_{} = {}".format(n, flist[-1])


print(first_fib_num_to_have_x_digits(1000))
print(time()-start)
