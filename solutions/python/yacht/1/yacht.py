# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == YACHT:
        if len(set(dice)) == 1:
            return 50
        else:
            return 0
    if category == ONES:
        return dice.count(1)
    if category == TWOS:
        return dice.count(2) * 2
    if category == THREES:
        return dice.count(3) * 3
    if category == FOURS:
        return dice.count(4) * 4
    if category == FIVES:
        return dice.count(5) * 5
    if category == SIXES:
        return dice.count(6) * 6
    if category == FULL_HOUSE:
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
            return sum(dice)
        else:
            return 0
    if category == FOUR_OF_A_KIND:
        if len(set(dice)) == 2:
            if dice.count(dice[0]) == 1:
                return dice[1] * 4
            elif dice.count(dice[0]) == 4:
                return dice[0] * 4
            else:
                return 0
        elif len(set(dice)) == 1:
            return dice[0] * 4
        else:
            return 0
    if category == LITTLE_STRAIGHT:
        if set(dice) == {1,2,3,4,5}:
            return 30
        else:
            return 0
    if category == BIG_STRAIGHT:
        if set(dice) == {2,3,4,5,6}:
            return 30
        else:
            return 0
    if category == CHOICE:
        return sum(dice)
