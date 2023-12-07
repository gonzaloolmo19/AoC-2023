from enum import Enum
from functools import cmp_to_key


card_values = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


class Kind(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


def parse_input(file):
    with open(file) as f:
        lines = [[x for x in line.split()] for line in f.readlines()]
        result = []
        for i in range(len(lines)):
            result.append([lines[i][0], int(lines[i][1])])
        return result


# En esta funcion es donde esta el error, porque muchas veces se coge dos veces la misma J para formar grupos
# Una idea es borrar las J del array, habiendo guardado su numero de apariciones en una variable
def getKind(_hand) -> Kind:
    hand = _hand.copy()
    cards_processed = ["J"]
    num_j = hand[0].count("J")
    hand[0].replace("J", "")
    groups_found = [0]

    for i in range(len(hand[0])):
        count = hand[0].count(hand[0][i])
        if num_j == 0:
            if count > 1 and hand[0][i] not in cards_processed:
                cards_processed.append(hand[0][i])
                groups_found.append(count)
        else:
            if count > 0 and hand[0][i] not in cards_processed:
                cards_processed.append(hand[0][i])
                groups_found.append(count)

    if len(groups_found) == 1:
        return Kind.HIGH_CARD
    if num_j == 5:
        return Kind.FIVE_OF_A_KIND
    elif max(groups_found) + num_j == 5:
        return Kind.FIVE_OF_A_KIND
    elif max(groups_found) + num_j == 4:
        return Kind.FOUR_OF_A_KIND
    elif max(groups_found) + num_j == 3 and 2 in groups_found:
        return Kind.FULL_HOUSE
    elif max(groups_found) + num_j == 3:
        return Kind.THREE_OF_A_KIND
    elif max(groups_found) + num_j == 2 and 2 in groups_found:
        return Kind.TWO_PAIRS
    elif max(groups_found) + num_j == 2:
        return Kind.ONE_PAIR
    else:
        return Kind.HIGH_CARD


def cmp_hand(hand1: str, hand2: str):
    if getKind(hand1).value > getKind(hand2).value:
        return 1
    elif getKind(hand1).value < getKind(hand2).value:
        return -1
    else:
        # En este caso las manos tienen el mismo tipo
        i = 0
        while hand1[0][i] == hand2[0][i]:
            i += 1
        if card_values[hand1[0][i]] > card_values[hand2[0][i]]:
            return 1
        elif card_values[hand1[0][i]] < card_values[hand2[0][i]]:
            return -1
        else:
            return 0


def part2():
    file = "input.txt"
    hands = parse_input(file)
    for hand in hands:
        print(hand, getKind(hand))

    hands = sorted(hands, key=cmp_to_key(cmp_hand))

    solution = 0
    for i, hand in enumerate(hands):
        solution += hand[1] * (i + 1)

    return solution


print("La solución a la parte 2 es:", part2())
