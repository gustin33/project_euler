from time import time
start = time()
"""
This was a strenuous problem:
Basically one has to note that for every n in 13 to 19 you add the number of
letters in n-10 + 4=number of letters in "teen", with some exceptions.
For numbers of the form 10*n with n=2,...9 you do the same, this time adding 2=# letters in "ty".
For a random number abc you must add:
g(a) + g(100) + 3 + g(bc)
Where g is the function that takes a number and outputs the number of letters of said number.
The 3 comes from the "and" part.
If bc=00, then g(bc) = 0.
"""


def g(a):
    if a <= 99:
        if a <= 10:
            if a < 3 or a == 6 or a == 10:
                return 3
            elif a == 4 or a == 5 or a == 9:
                return 4
            else:
                return 5
        elif 10 < a < 13 or a == 20:
            return 6
        elif a == 18 or a == 13 or a == 15:
            return g(a-10) + 3
        elif 16 <= a <= 17 or a == 19 or a == 14:
            return g(a-10) + 4
        elif a in [10*x for x in range(6, 8)] or a == 90:
            return g(int(a/10))+2
        elif a == 30 or a == 80 or a == 40 or a == 50:
            return g(int(a/10)) + 1
        else:
            return g(10*int(a/10)) + g(a-10*int(a/10))
    elif a == 1000:
        return g(1) + 8
    elif a in [100*x for x in range(1, 10)]:
        return g(int(a/100)) + 7
    else:
        return g(int(a/100)) + 10 + g(a - 100*int(a/100))


s = 0
for num in range(1, 1001):
    s += g(num)
print(s)
print(time()-start)
