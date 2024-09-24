import random
from collections import defaultdict

# Board constants
GO = 0
JAIL = 10
G2J = 30
CC = [2, 17, 33]  # Community Chest squares
CH = [7, 22, 36]  # Chance squares
RAILROADS = [5, 15, 25, 35]
UTILITIES = [12, 28]

# Community Chest cards
CC_CARDS = [GO, JAIL] + [None] * 14

# Chance cards
CH_CARDS = [GO, JAIL, 11, 24, 39, RAILROADS[0], 'R', 'R', 'U', -3] + [None] * 6

# Simulation parameters
NUM_SQUARES = 40
NUM_SIMULATIONS = 10**6

def roll_dice():
    """Simulates rolling two 4-sided dice."""
    die1 = random.randint(1, 4)
    die2 = random.randint(1, 4)
    return die1, die2

def move_to_next_railroad(pos):
    """Move to the next railroad square."""
    return next(r for r in RAILROADS if r > pos) if any(r > pos for r in RAILROADS) else RAILROADS[0]

def move_to_next_utility(pos):
    """Move to the next utility square."""
    return next(u for u in UTILITIES if u > pos) if any(u > pos for u in UTILITIES) else UTILITIES[0]

def process_chance(pos):
    """Process Chance card effects."""
    card = random.choice(CH_CARDS)
    if card is None:
        return pos  # No movement
    elif card == 'R':
        return move_to_next_railroad(pos)
    elif card == 'U':
        return move_to_next_utility(pos)
    elif card == -3:
        return (pos - 3) % NUM_SQUARES
    else:
        return card

def process_community_chest(pos):
    """Process Community Chest card effects."""
    card = random.choice(CC_CARDS)
    return pos if card is None else card

def simulate_monopoly():
    # Initialize counters for each square
    square_visits = defaultdict(int)

    # Start at GO
    pos = GO
    consecutive_doubles = 0

    for _ in range(NUM_SIMULATIONS):
        die1, die2 = roll_dice()
        doubles = die1 == die2

        if doubles:
            consecutive_doubles += 1
        else:
            consecutive_doubles = 0

        # If three consecutive doubles, go to Jail
        if consecutive_doubles == 3:
            pos = JAIL
            consecutive_doubles = 0
        else:
            # Move the player
            pos = (pos + die1 + die2) % NUM_SQUARES

            # Handle special squares
            if pos == G2J:
                pos = JAIL
            elif pos in CC:
                pos = process_community_chest(pos)
            elif pos in CH:
                pos = process_chance(pos)

        # Record the visit
        square_visits[pos] += 1

    # Convert visit counts to percentages
    for square in square_visits:
        square_visits[square] = (square_visits[square] / NUM_SIMULATIONS) * 100

    # Get the three most visited squares
    most_visited = sorted(square_visits.items(), key=lambda x: -x[1])[:3]
    return ''.join(f'{square:02d}' for square, _ in most_visited)

# Run the simulation
print(simulate_monopoly())
