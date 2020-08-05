from time import time
start = time()
file = open("p022_names.txt", "r").read()
names = [line.strip("\"") for line in file.split(",")]
names.sort()


def value_of_word(n):
    def ord_of_letters(x):
        return ord(x) - 64
    return sum(list(map(ord_of_letters, list(n))))


S = 0
for i in names:
    S += value_of_word(i)*(1+names.index(i))
print(S)
print(time()-start)
