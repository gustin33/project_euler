from math import sqrt, floor
partition_list = [1, 1]

m = 8

i = 2

indices = [1, 2]
while i < m:
    print(i)
    print(1, indices)
    if sqrt(1+24*i) == floor(sqrt(1+24*i)):
        indices.append(i)
    print(2, partition_list)
    print()
    partition_list.append(sum(partition_list[-i] for i in indices))
    i += 1

print(partition_list)