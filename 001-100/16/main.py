def sum_of_digits(n):  # sum of digits is nmod10 + (n-nmod10)//10 mod 10 + ...
    m = n
    b = n % 10
    sum_digits = 0
    counter = 0
    while m != b:
        print(m, b)
        m = (m - b) // 10^counter
        b += m % 10
        sum_digits += b
        counter += 1
    return sum_digits
print(sum_of_digits(2**15))
