from time import time
start = time()


def is_int(x):
    return x == int(x)


N = 1
n = 1
s = 0
while True:
    pentagonal = (1+(1+24*N)**0.5)/6
    hexagonal = (1+(1+8*N)**0.5)/4
    if is_int(pentagonal) and is_int(hexagonal):
        print("T_{} = P_{} = H_{} = {}".format(n, int(pentagonal), int(hexagonal), N))
        s += 1
    if s == 3:
        break
    N += n+1
    n += 1
print(time()-start)
