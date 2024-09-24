import itertools

# The square numbers that we want to form
squares = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]

# Account for the fact that 6 and 9 can be used interchangeably
def can_form_all_squares(cube1, cube2):
    for d1, d2 in squares:
        if not (((d1 in cube1 or (d1 == 6 and 9 in cube1) or (d1 == 9 and 6 in cube1)) and
                 (d2 in cube2 or (d2 == 6 and 9 in cube2) or (d2 == 9 and 6 in cube2))) or
                ((d1 in cube2 or (d1 == 6 and 9 in cube2) or (d1 == 9 and 6 in cube2)) and
                 (d2 in cube1 or (d2 == 6 and 9 in cube1) or (d2 == 9 and 6 in cube1)))):
            return False
    return True

def count_valid_cube_arrangements():
    # Generate all combinations of 6 digits from {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    digits = list(range(10))
    cube_combinations = list(itertools.combinations(digits, 6))
    
    valid_pairs = set()

    # Check all pairs of cubes
    for cube1 in cube_combinations:
        for cube2 in cube_combinations:
            # Sort the cubes to avoid duplicate pairs (since the order doesn't matter)
            if can_form_all_squares(cube1, cube2):
                valid_pairs.add(tuple(sorted([cube1, cube2])))

    return len(valid_pairs)

# Run the simulation
print(count_valid_cube_arrangements())
