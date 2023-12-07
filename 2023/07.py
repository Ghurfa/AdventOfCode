def all_eq(lis):
    for x in lis:
        if (x != 'J') and (x != lis[0]):
            return False
    else:
        return True

def get_type(hand: str) -> int:
    cards = ''.join(sorted(hand))
    if all_eq(cards):
        return 0
    elif all_eq(cards[1:]) or all_eq(cards[:-1]):
        return 1
    elif (all_eq(cards[:2]) and all_eq(cards[2:])) or (all_eq(cards[:3]) and all_eq(cards[3:])):
        return 2
    elif all_eq(cards[:3]) or all_eq(cards[1:4]) or all_eq(cards[2:]):
        return 3
    elif (all_eq(cards[:2]) and all_eq(cards[2:4])) or (all_eq(cards[:2]) and all_eq(cards[3:])) or (all_eq(cards[1:3]) and all_eq(cards[3:])):
        return 4
    elif all_eq(cards[:2]) or all_eq(cards[1:3]) or all_eq(cards[2:4]) or all_eq(cards[3:]):
        return 5
    else:
        return 6
    
def get_best_type(hand: str) -> int:
    letters = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    best = 7
    for letter in letters:
        replaced = hand.replace('J', letter)
        score = get_type(replaced)
        best = min(best, score)
    return best

def compare_card(card: str) -> int:
    scores = {
        'A': 0,
        'K': 1,
        'Q': 2,
        'J': 13,
        'T': 4,
        '9': 5,
        '8': 6,
        '7': 7,
        '6': 8,
        '5': 9,
        '4': 10,
        '3': 11,
        '2': 12,
    }
    return scores[card]


def main():
    lines = []
    with open("07-input.txt", encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    hands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]
    
    # Part 1 version
    # hands.sort(key=lambda x: (get_type(x[0]), compare_card(x[0][0]), compare_card(x[0][1]), compare_card(x[0][2]), compare_card(x[0][3]), compare_card(x[0][4])))

    # Part 2 version
    hands.sort(key=lambda x: (get_best_type(x[0]), compare_card(x[0][0]), compare_card(x[0][1]), compare_card(x[0][2]), compare_card(x[0][3]), compare_card(x[0][4])))
    
    winnings = [(len(hands) - i) * hands[i][1] for i in range(0, len(hands))]
    print(sum(winnings))

if __name__ == "__main__":
    main()
