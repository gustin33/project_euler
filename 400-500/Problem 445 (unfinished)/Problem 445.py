                                                   #445(unfinished)
import time
import math
from math import factorial as ft
start = time.time()
def R(n):
    S = 0
    for a in range(1,n):
        b = 0
        while b < n:
            if a * b % n == 0 and a*(a-1) % n == 0:
                S += 1
                b += 1
            b += 1
    return S
def F(N):
    list = []
    for k in range(1,N+1):
        list.append(R(ft(N+1)//ft(k) //ft(N+1-k)))
    return sum(list)

print(R(10000000))

#for N in range(1,21):
#    list1 = []
#    for k in range(1,(N+1)//2+1):
#        list1.append(R(ft(N+1)//ft(k)//ft(N+1-k)))
#    print("{}: ".format(N),list1)
