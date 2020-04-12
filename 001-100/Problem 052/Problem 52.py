from time import time
start = time()
x = 1
while not(set(str(x)) == set(str(2*x)) and set(str(x)) == set(str(3*x)) and
          set(str(x)) == set(str(4*x)) and set(str(x)) == set(str(5*x)) and set(str(x)) == set(str(6*x))):
    x += 1

print('The smallest positive integer x is %s' %x)
print('And 2x, 3x, ... 6x are:')
for i in range(2, 7):
    print('%sx: '%i, i*x)
print(time()-start)
