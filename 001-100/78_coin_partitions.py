def partition_function(limit, modulo):
    # Array to store partition numbers p(n)
    partitions = [0] * (limit + 1)
    partitions[0] = 1  # p(0) = 1

    pentagonal = lambda k: k * (3 * k - 1) // 2  # Generalized pentagonal number formula

    for n in range(1, limit + 1):
        total = 0
        k = 1
        sign = 1  # Alternates between + and -

        while True:
            pent_k = pentagonal(k)
            if pent_k > n:
                break
            total += sign * partitions[n - pent_k]

            pent_neg_k = pentagonal(-k)
            if pent_neg_k > n:
                break
            total += sign * partitions[n - pent_neg_k]

            sign *= -1
            k += 1

        partitions[n] = total % modulo  # Modulo to avoid large numbers

        if partitions[n] == 0:
            return n

    return -1  # If no such n is found within the limit

if __name__ == "__main__":
    modulo = 10**6  # Looking for p(n) divisible by 1 million
    limit = 100000  # Initial upper limit for search
    result = partition_function(limit, modulo)
    print("The least value of n for which p(n) is divisible by one million is:", result)
