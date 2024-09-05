# Minimal Roman numerals representation
def to_minimal_roman(n):
    value_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""
    for value, numeral in value_map:
        while n >= value:
            result += numeral
            n -= value
    return result


# Read Roman numerals from file and calculate characters saved
def calculate_characters_saved(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    total_saved = 0

    for line in lines:
        original = line.strip()
        value = roman_to_int(original)
        minimal = to_minimal_roman(value)
        total_saved += len(original) - len(minimal)

    return total_saved


# Convert Roman numeral to integer
def roman_to_int(s):
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total


# Define the file path and calculate the result
file_path = "89_input.txt"
result = calculate_characters_saved(file_path)
print(f"Total characters saved: {result}")
