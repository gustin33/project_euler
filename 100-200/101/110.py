import math
from tqdm import tqdm

"""
We have 

1/x + 1/y = 1/n --> nx+ny = xy --> (x-n)(y-n) = n^2

Then the number of solutions is given by the number of divisors of n^2. If we want the 
unique solutions (for example, taking x<=y) we need have:
#sol = ( prod(1+2alpha_i) - 1 )// 2

Where n = prod p_i ^ alpha_i

Since we need #sol > N, then

divisores = prod > 2*N+1

We are looking for a number divisores which is highly composite (check https://mathworld.wolfram.com/HighlyCompositeNumber.html) this means that 
d(divisores) is greater than d(m) for all m < divisores (d is # of divisors). 
From the previous page we know that divisores must satisfy:

1- divisores = 2^a1 3^a2 ... p^am, where 2,3,...,p form a string of consecutive primes
2- a1 >= a2 >=....>= am 

Under these conditions, n is minimum (conjecture)
"""

PRIMOS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def divisores_cuadrado(n):
    contador = 1

    primo = 2

    while n > 1:
        if n % primo == 0:
            alfa = 0
            while n % primo == 0:
                n /= primo
                alfa += 1
            contador *= 1 + 2 * alfa
        primo += 1
    return contador


N = 4 * 10**6

divisores = 2 * N - 1
divisores += 3 - ((2 * N - 1) % 3)  # this is done to find the lowest multiple of 3 bigger than 2*N-1

# We find the highest number above divisores that is highly composite
while True:
    m = divisores
    indice_primo = 0
    alpha = N
    while m > 1:
        primo = PRIMOS[1:][indice_primo]
        if m % primo != 0:
            break
        alpha_nuevo = 0
        while m % primo == 0:
            m /= primo
            alpha_nuevo += 1
        if alpha_nuevo > alpha:
            break
        alpha = alpha_nuevo

        indice_primo += 1

    if m == 1:
        break
    divisores += 6


def factorizacion_primos(n):
    factorizacion = []
    for primo in PRIMOS:
        if n % primo == 0:
            potencia = 0
            while n % primo == 0:
                n /= primo
                potencia += 1

            factorizacion.append((primo, potencia))
    return factorizacion


print(f"divisores: {divisores}")
print(f"factorizacion_primos(divisores): {factorizacion_primos(divisores)}")


n = 1
indice_primo = 0
for primo, potencia in reversed(factorizacion_primos(divisores)):
    print(f"primo: {primo}, potencia: {potencia}")
    exponente = (primo - 1) // 2

    for indice_potencia in range(potencia):
        print(f"{PRIMOS[indice_primo]} ** {exponente}")
        n *= PRIMOS[indice_primo] ** exponente
        indice_primo += 1

print(f"n: {n}")
