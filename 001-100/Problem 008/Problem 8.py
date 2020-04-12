from time import time
start = time()
def product_string(string):
    result = 1
    for number in string:
        result *= int(number)
    return result

def largest_product(numbers, adjacent):
    maximum_number = 0
    begin = 0
    while begin <= len(numbers)-adjacent:
        next_number = product_string(numbers[begin: begin + adjacent])
        if next_number > maximum_number:
            maximum_number = next_number
        begin += 1
    return maximum_number

file = open('input.txt')
string_of_numbers = ''.join([line.strip('\n') for line in file.readlines()])
print('The largest product for {} adjacent numbers is: {}'
      .format(4, largest_product(string_of_numbers, 4)))
print('The largest product for {} adjacent numbers is: {}'
      .format(13, largest_product(string_of_numbers, 13)))

print(time()-start)

