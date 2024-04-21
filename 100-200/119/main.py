import math


def digit_sum(n):
    return sum(int(i) for i in list(str(n)))


counter = 2

m = 3
while counter < 31:

    for sn in range(2, 9 * m + 1):
        log = math.log(10, sn)
        for k in range(math.ceil((m - 1) * log), math.floor(m * log) + 1):
            if sn == digit_sum(sn**k):
                print(f"a_{counter} = {sn**k}")
                counter += 1
    m += 1
