from enum import Enum
from functools import cmp_to_key


card_values = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
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


def getKind(_hand) -> Kind:
    hand = _hand.copy()
    cards_processed = []
    groups_found = []

    for i in range(len(hand[0])):
        count = hand[0].count(hand[0][i])
        if count > 1 and hand[0][i] not in cards_processed:
            cards_processed.append(hand[0][i])
            groups_found.append(count)

    if len(groups_found) == 1:
        if groups_found[0] == 2:
            return Kind.ONE_PAIR
        elif groups_found[0] == 3:
            return Kind.THREE_OF_A_KIND
        elif groups_found[0] == 4:
            return Kind.FOUR_OF_A_KIND
        else:
            return Kind.FIVE_OF_A_KIND
    elif len(groups_found) == 2:
        if groups_found[0] == 2 and groups_found[1] == 2:
            return Kind.TWO_PAIRS
        else:
            return Kind.FULL_HOUSE
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


def part1():
    file = "test1.txt"
    hands = parse_input(file)

    hands = sorted(hands, key=cmp_to_key(cmp_hand))

    solution = 0
    for i, hand in enumerate(hands):
        solution += hand[1] * (i + 1)

    return solution


print("La solución a la parte 1 es:", part1())
