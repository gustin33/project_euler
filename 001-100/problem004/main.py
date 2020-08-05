import itertools
import time
start = time.time()

candidates = []
for a,b,c in itertools.product(range(1,10), range(10), range(10)):
    candidates.append('{}{}{}'.format(a,b,a))
    candidates.append('{}{}{}{}'.format(a,b,b,a))
    candidates.append('{}{}{}{}{}'.format(a,b,c,b,a))
    candidates.append('{}{}{}{}{}{}'.format(a,b,c,c,b,a))

candidates = list(map(int,candidates))
candidates.sort()

flag = 0
for num in candidates[::-1]:
    for a in range(100, 1000):
        if num // a == num / a and num // a in range(100,1000):
            print(num)
            flag = 1
            break
    if flag:
        break
print(time.time()-start)
