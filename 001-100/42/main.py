from time import time
start = time()
file = open('p042_words.txt', 'r').read()
print(file.split(','))
words = [line.strip('"') for line in file.split(',')]
print(words)
s = 0
for a in [sum([ord(b)-64 for b in list(a)]) for a in words]:
    if a in [int(n*(n+1)/2) for n in range(1, 28)]:
        s += 1
print(s)
print(time()-start)
