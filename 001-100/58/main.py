def isPrime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            return False
    return True

def a(n): return 1+2*(n//4+1)*(2*(n//4) + n%4)
l = 7
numerator = 8
while (numerator*10 >= 2*l-1):
    l+=2
    for n in range(2*(l-3), 2*(l-1)+1):
        if isPrime(a(n)):
            numerator += 1
print(f"l: {l}")
