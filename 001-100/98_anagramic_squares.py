import itertools
from collections import defaultdict
from tqdm import tqdm

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = set(word.strip().upper() for word in file)
    return words

def generate_square_numbers(max_length):
    square_numbers = []
    limit = 10 ** max_length
    i = 1
    while i * i < limit:
        square_numbers.append(i * i)
        i += 1
    return square_numbers

def get_square_number_set(square_numbers):
    return set(square_numbers)

def convert_word_to_number(word):
    # Convert each character to its position in the alphabet (1-9 for A-I, 0 for J-Z)
    return int(''.join(str(ord(char) - ord('A') + 1) for char in word))

def find_largest_square_anagram(words):
    max_length = max(len(word) for word in words)
    square_numbers = generate_square_numbers(max_length)
    square_number_set = get_square_number_set(square_numbers)

    # Create a dictionary for sorted letters to word list
    sorted_word_map = defaultdict(set)
    for word in words:
        sorted_word = ''.join(sorted(word))
        sorted_word_map[sorted_word].add(word)

    largest_square = 0

    # Use tqdm to add a progress bar
    for word1 in tqdm(words, desc="Processing words"):
        sorted_word1 = ''.join(sorted(word1))
        for word2 in sorted_word_map[sorted_word1]:
            if word1 != word2:  # Ensure word1 and word2 are different
                num1 = convert_word_to_number(word1)
                num2 = convert_word_to_number(word2)

                if num1 in square_number_set and num2 in square_number_set:
                    largest_square = max(largest_square, num1, num2)

    return largest_square

# Load words and execute the function
file_path = '98_input.txt'
words = load_words(file_path)

largest_square = find_largest_square_anagram(words)
print(f"Largest square number formed by any member of a square anagram word pair: {largest_square}")
