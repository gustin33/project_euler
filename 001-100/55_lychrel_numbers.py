def reverse(n):
    return int(str(n)[::-1])

def isLychrel(n):
    for i in range(50):
        n += reverse(n)
        if n == reverse(n):
            return 0
    return 1

print(sum(isLychrel(n) for n in range(10000)))
