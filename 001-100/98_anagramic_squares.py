def wordchecker(word, number):
    word_fingerprint = []
    for x in word:
        word_fingerprint.append(word.count(x))
    
    number_fingerprint = []
    for x in number:
        number_fingerprint.append(number.count(x))
        
    return word_fingerprint == number_fingerprint

def compute(words):
    candidates = []
    
    for x in range(len(words)):
        for y in range(x+1, len(words)):
            if sorted(list(words[x])) == sorted(list(words[y])):
                candidates.append((len(words[x]), (words[x], words[y])))
    
    candidates = sorted(candidates, reverse=True)
    possiblesquares = [str(x**2) for x in range(1, 31623)]
    
    max_square = 0
    for x in candidates:
        for y in possiblesquares:
            length = len(y)
            if length > x[0]:
                break
            
            if length == x[0]:
                word = x[1][0]
                if wordchecker(word, y):
                    temp_dict = {}
                    for z in range(len(word)):
                        if word[z] not in temp_dict:
                            temp_dict[word[z]] = y[z]
                    
                    number = ""
                    for a in x[1][1]:
                        number += temp_dict[a]
                    
                    if number in possiblesquares:
                        max_square = max(max_square, int(y), int(number))

    return max_square

# Read words from 98_input.txt
with open('98_input.txt', 'r') as file:
    words = [word.strip().strip('"') for word in file.readline().split(',')]

# Compute the maximum square number formed by anagram pairs
result = compute(words)
print("Largest square formed by any member of an anagram pair:", result)
