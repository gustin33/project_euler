from time import time
start = time()
def summation_of_primes(n):
    numbers = list(range(2,n+1))
    while True:
        prime = numbers[0]
        print(prime)
        if prime > n**0.5:
            break
        for index, num in enumerate(numbers[1:]):
            if num % prime == 0:
                print(num,index, numbers)
                del numbers[index+1]
    return sum(primes)

print(summation_of_primes(10))
#print(summation_of_primes(2*10**6))
print(time()-start)
