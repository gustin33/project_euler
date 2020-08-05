import itertools
# v-gon:
v = 5


def comb(n):  # combinations of 1,2,..,10 that add to n
    return [set(combination) for combination in list(itertools.combinations(list(range(1, 2*v+1)), 3))
            if sum(combination) == n]


i = 11
while i <= 20:
    print(i, len(comb(i)))
    print(comb(i))
    i += 1


def center(n):
    return [list(comb(n)[j[0]].intersection(comb(n)[j[1]]))[0] for j in list(itertools.combinations([0, 1, 2], 2))]


def exterior(n):
    return [number for number in range(1, 2*v+1) if number not in center(n)]


def concatenated_number(n):  # returns maximum concatenated number
    first_digit = min(exterior(n))
    list_of_elements = []
    element1 = []
    combinations = comb(n)
    for combination in combinations:
        if first_digit in combination:
            a = combination
            element1.append(first_digit)
            list_num = []
            for num in a:
                if num != first_digit:
                    list_num.append(num)
            element1.append(max(list_num))
            for num in a:
                if num not in element1:
                    element1.append(num)
    list_of_elements.append(element1)
    i = 2
    while i <= v:
        element_i__1 = list_of_elements[-1]
        element_i = []
        for combination in combinations:
            if element_i__1[-1] in combination and combination != set(element_i__1):
                for number in combination:
                    if number in exterior(n):
                        element_i.append(number)
                        element_i.append(element_i__1[-1])
                for number in combination:
                    if number not in element_i:
                        element_i.append(number)
        list_of_elements.append(element_i)
        i += 1
    concatenated_num = []
    for element in list_of_elements:
        concatenated_num += element
    return int("".join([str(number) for number in concatenated_num]))


def list_of_totals():
    n = 1
    while len(comb(n)) < v:
        n += 1
    a = n
    while len(comb(n)) == v:
        n += 1
    b = n
    return list(range(a, b))


def maximum_string():
    return max([concatenated_number(num) for num in list_of_totals()])


print(maximum_string())

