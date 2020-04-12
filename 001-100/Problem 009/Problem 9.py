import itertools

m = 1000
for a,b in itertools.product(range(1,m+1),range(1,m+1)):
    c = m-a-b
    if a**2+b**2 == c**2:
        print(a*b*c)
        break
