from collections import Counter

# Map from card ranks to numerical values
CARD_VALUES = {str(i): i for i in range(2, 10)}
CARD_VALUES.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})

def parse_hand(hand):
    """Parse a hand of 5 cards, return a list of tuples (value, suit)."""
    return [(CARD_VALUES[card[0]], card[1]) for card in hand.split()]

def hand_rank(hand):
    """Return a tuple representing the rank of the hand, for comparison."""
    values = sorted([value for value, suit in hand], reverse=True)
    suits = [suit for value, suit in hand]
    
    value_counts = Counter(values)
    unique_values = sorted(set(values), reverse=True)
    
    is_flush = len(set(suits)) == 1
    is_straight = len(unique_values) == 5 and unique_values[0] - unique_values[4] == 4
    
    # Royal Flush
    if is_flush and values == [14, 13, 12, 11, 10]:
        return (10,)
    
    # Straight Flush
    if is_flush and is_straight:
        return (9, values[0])
    
    # Four of a Kind
    if 4 in value_counts.values():
        four_kind_value = [v for v, count in value_counts.items() if count == 4][0]
        kicker = [v for v in values if v != four_kind_value]
        return (8, four_kind_value, kicker[0])
    
    # Full House
    if 3 in value_counts.values() and 2 in value_counts.values():
        three_kind_value = [v for v, count in value_counts.items() if count == 3][0]
        pair_value = [v for v, count in value_counts.items() if count == 2][0]
        return (7, three_kind_value, pair_value)
    
    # Flush
    if is_flush:
        return (6, values)
    
    # Straight
    if is_straight:
        return (5, values[0])
    
    # Three of a Kind
    if 3 in value_counts.values():
        three_kind_value = [v for v, count in value_counts.items() if count == 3][0]
        kickers = [v for v in values if v != three_kind_value]
        return (4, three_kind_value, kickers)
    
    # Two Pairs
    if list(value_counts.values()).count(2) == 2:
        pairs = sorted([v for v, count in value_counts.items() if count == 2], reverse=True)
        kicker = [v for v in values if v not in pairs][0]
        return (3, pairs[0], pairs[1], kicker)
    
    # One Pair
    if 2 in value_counts.values():
        pair_value = [v for v, count in value_counts.items() if count == 2][0]
        kickers = [v for v in values if v != pair_value]
        return (2, pair_value, kickers)
    
    # High Card
    return (1, values)

def compare_hands(hand1, hand2):
    """Compare two hands and return 1 if hand1 wins, 2 if hand2 wins, 0 if tie."""
    rank1 = hand_rank(hand1)
    rank2 = hand_rank(hand2)
    
    if rank1 > rank2:
        return 1
    elif rank2 > rank1:
        return 2
    else:
        return 0

def count_player1_wins(filename):
    player1_wins = 0
    
    with open(filename, 'r') as file:
        for line in file:
            cards = line.strip().split()
            player1_hand = parse_hand(' '.join(cards[:5]))
            player2_hand = parse_hand(' '.join(cards[5:]))
            
            winner = compare_hands(player1_hand, player2_hand)
            if winner == 1:
                player1_wins += 1
                
    return player1_wins

# Count Player 1's wins
filename = '54_input.txt'
result = count_player1_wins(filename)
print(f"Player 1 wins {result} hands.")
