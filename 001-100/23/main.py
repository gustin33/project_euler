LIMIT = 28123
sum_divisors = [1]*(LIMIT + 1)
sum_divisors[0] = 0
for i in range(2, LIMIT+1):
    j = 2
    while (j*i < LIMIT+1):
        sum_divisors[j*i] += i
        j += 1
abundant_numbers = [num for num in range(1, LIMIT) if sum_divisors[num] > num]
rang = [1] * (LIMIT+1)
for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        if abundant_numbers[i] + abundant_numbers[j] <= LIMIT:
            rang[abundant_numbers[i] + abundant_numbers[j]] = 0

print(sum(num for num in range(1, LIMIT+1) if rang[num] == 1))

