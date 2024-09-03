def count_partitions(n):
    # Create an array to store the partition counts
    partitions = [0] * (n + 1)
    partitions[0] = 1  # There is one way to partition 0 (using no parts)

    # Iterate over each integer from 1 to n
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    return partitions[n]


# Calculate the number of partitions of 100
n = 100
partitions_count = count_partitions(n)

# We subtract 1 to exclude the partition that is just 100 itself
result = partitions_count - 1

# Print the result
print(
    f"The number of different ways to write 100 as a sum of at least two positive integers is: {result}"
)
