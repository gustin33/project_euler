from math import factorial as fact
from tqdm import tqdm

chain_representatives = {}


def factorial_digit(n):
    return sum(map(lambda digit: fact(int(digit)), list(str(n))))


n = 6
MAX = 10**n
count_lenght_of_chain = 0
length_of_chain_searched = 61

numbers = [0]*(fact(9)*6+1)

for i in tqdm(range(1, MAX)):
    curr = i
    previous = []
    while True:
        # print(f"count:{count}")
        previous.append(curr)
        curr = factorial_digit(curr)
        if curr in previous:
            curr_index = previous.index(curr)
            chain_length = len(previous) - curr_index

            same_length = previous[curr_index:]
            diff_length = previous[:curr_index]
            
            if length_of_chain_searched - chain_length == 0:
                count_lenght_of_chain+=len(same_length)
            elif length_of_chain_searched - chain_length <= len(diff_length):
                count_lenght_of_chain+=1

            for number in same_length:
                numbers[number] = chain_length

            count = 1   
            for number in reversed(diff_length):
                numbers[number] = chain_length + count
                count+=1
            break

# print(numbers[:MAX])
# print(numbers[1454])
print(f"count for {length_of_chain_searched}: {count}")
