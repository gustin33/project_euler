from time import time as t
# let the n-th approximation be 1+b_n = 1 + a_n / c_n
# then a_n = c_n-1
# c_n+1 = 2*c_n + c_n-1
# so the aprox is 1+b_n = (c_n+c_n-1)/c_n


def first_x_cterms(x):
    list_c = [1, 2]
    j = 2
    while j < x:
        list_c.append(2*list_c[j-1]+list_c[j-2])
        j += 1
    return list_c


def number_of_digits(n):
    return len(list(str(n)))


def number_of_fractions(n):
    n += 1
    list1 = first_x_cterms(n)
    s = 0
    for num in range(1, n):
        numerator = list1[num-1] + list1[num]
        denominator = list1[num]
        if number_of_digits(numerator) > number_of_digits(denominator):
            s += 1
    return s


d = 1000
while d <= 10000:
    start = t()
    print('''For numbers less than {}, the number of fractions which contain
            a numerator with more digits than the denominator is {}.\
     Time elapsed: {}\n'''.format(d, number_of_fractions(d), t()-start))
    d += 1000

