digits = ['1','2','3','4','5','6','7','8','9','0']
divisors = [13, 11, 7, 5, 3, 2, 1]
res = []
res1 = []

j = 1
while j*17 < 1000:
    N = j*17
    Nstr = str(N)
    if len(set(Nstr)) == len(Nstr):
        if N < 100: res.append('0' + str(N))
        else: res.append(str(N))
    j += 1

for div in divisors:
    for Nstr in res:
        for d in digits:
            if d not in Nstr:
                Newstr = d + Nstr[:2]
                if int(Newstr)%div == 0:
                    res1.append(d + Nstr)

    res = res1
    res1 = []

tot = 0
i = 1
for Nstr in res:
    print(f"{i}: {Nstr}")
    tot += int(Nstr)
    i+=1
print()
print(f"sum: {tot}")
