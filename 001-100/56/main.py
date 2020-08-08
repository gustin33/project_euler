def digital_sum(c):
    return sum(int(a) for a in str(c))

maximum_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        res = digital_sum(a**b)
        if res > maximum_sum:
            maximum_sum = res
print(maximum_sum)
