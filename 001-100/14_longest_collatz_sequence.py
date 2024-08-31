def chain_collatz(n):
    m = n
    chain = 1
    while True:
        if m == 1:
            break
        elif m % 2 == 0:
            m = m//2
        else:
            m = 3*m+1
        chain += 1
    return chain

chains = [0] * 10**6
chains[:2] = [1,2]  # 1 -> 1 has one term, 2 -> 1 -> 1 has two terms
num = 3
while num <= 10**6:
    m = num
    chain = 1
    while True:
        if m % 2 == 0:
            if m // 2 in 

        else:
            
        elif m % 2 == 0:
            m = m//2
        else:
            m = 3*m+1
        chain += 1

    if z > longest_chain[1]:
        longest_chain[1] = z
        longest_chain[0] = num
    print(num)
    num += 1
print(longest_chain[0])
