"cat numbers.txt | paste -sd+ | bc -l| awk '{print substr($0, 0, 11)}'"
file = open('13_input.txt','r').read()
numbers = [int(line) for line in file.split('\n')]
S = sum(numbers)
print(str(S)[:10])
