                                                   #92(unfinished)
from time import time as t
import itertools
start = t()


def sum_squares_num(n):
    s = 0
    for digit in list(map(int, list(str(n)))):
        s += digit**2
    return s


def square_digit(x):
    if x == 1:
        return 1  # 1 can be used as a boolean value "True"
    elif x == 89:
        return 0  # 0 can be used as a False boolean value, as well
    else:
        return square_digit(sum_squares_num(x))


def square_digit_list_1(n):  # returns a list of numbers <= n which end in 1
    flags = [0]*(n+1)  # list representing all numbers going to 1 (value 1) or 89 (value 0)
    for number in range(1, n+1):
        num = int("".join([digit for digit in list(str(number)) if digit != "0"]))  # This code filters 0´s out of
        if square_digit(num) and flags[num] == 0:  # if the number is possibly not a permutation of a smaller one
                # the number, given that they do not contribute to the addition of squares.
                digits = list(str(number))  # We use here number and num, since we want to eliminate all possibilities
                digitss = list(str(num))
                permutations_of_num = list(itertools.permutations(digitss, len(digitss)))
                permutations_of_number = list(itertools.permutations(digits, len(digits)))  # ,including and excluding 0´s.
                all_permutations = permutations_of_num + permutations_of_number
                for perm in [int("".join(perm)) for perm in all_permutations]:
                    if perm < n + 1:  # These lines of code sets all permutations of num to 1 in flags, provided
                        flags[perm] = 1  # they´re less than n+1.
    return sum(flags)
n = 10**6
print(square_digit_list_1(n))
print(t()-start)
