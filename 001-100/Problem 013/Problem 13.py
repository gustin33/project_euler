file = open('input.txt','r').read()
numbers = [int(line) for line in file.split('\n')]
S = sum(numbers)
print(str(S)[:10])
