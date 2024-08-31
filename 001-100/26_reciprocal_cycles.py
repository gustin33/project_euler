from time import time
from math import *
start = time()
###
def decimal_representation(p, q):  # returns 0.abc...(defg...) where the part in parentheses indicates the
    # repeating decimal cycle of the fraction p/q
    r = p // gcd(p, q)
    s = q // gcd(p, q)
    b_n = [r % s]
    decimal_part = ""
    representation = str(r//s)
    flag = 1
    while True:
        for bb in b_n:
            if bb == 10 * b_n[-1] % s:
                decimal_part += str(10 * b_n[-1] // s)
                flag = 0
                b_index = b_n.index(bb)
                representation += "," + decimal_part[0:b_index]  # this part we´re adding is the non-repeating
                # decimal part
                decimal_part = decimal_part[b_index:]  # decimal_part becomes the repeating part of the decimal repr
                break
        if flag:
            decimal_part += str(10*b_n[-1]//s)
            b_n.append(10*b_n[-1] % s)
        else:
            break
    if b_n[-1] != 0:
        representation += "(" + decimal_part + ")"
    if b_n[0] == 0:
        return representation + "0"
    return len(representation), representation
###


z = 10**3
per_len_list = []
for d in range(2, z):
    per_len_list.append(decimal_representation(1, d)[0])
    print("{}: {}".format(d, decimal_representation(1, d)[0]))
print("The number that produces the maximum recurring cycle under {} is {}. With a length of {}".
      format(z, 2 + per_len_list.index(max(per_len_list)), max(per_len_list)))  # 0 corresponds to 2
print("Its decimal representation is: {}".format(decimal_representation
                                                 (1, 2 + per_len_list.index(max(per_len_list)))[1]))
print(time()-start)
