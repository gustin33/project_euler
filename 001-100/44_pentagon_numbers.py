from math import sqrt
c = 1
i = D = 0
while c:
    D += 3*i+1
    i+=1
    Pd = 0
    for d in range(1, i):
        Pd += 3*d-2
        j, r = divmod(D-Pd, 3*d)
        if (not r) and not (1+sqrt(1+24*(j*(3*j-1)+D)))%6:
            print(D)
            c-=1
