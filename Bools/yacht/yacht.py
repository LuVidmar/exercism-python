"""
This module only contains a function to indicate the score of a given list of dices
"""

# Score categories.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice: list, category: int) -> int:
    """
    Given a list for five dice and a category, return the score

    :parameter: dice: list - list with dice rolls
    :parameter: category: int - chosen category
    :return: int - score
    """

    dice.sort() #sort for better processing

    # dice validation
    for d in dice:
        if d < 1 or d > 6:
            raise ValueError("Dice should be between 1 and 6")
        
    # return value according to table
    if category == YACHT:
        if quantity_of_number(dice, repeated_number(dice)[0]) == 5: #category matches
            return 50
        else:
            return 0
    elif category == CHOICE:
        return sum(dice)
    elif category == BIG_STRAIGHT:
        if dice == [2,3,4,5,6]: #category matches
            return 30
        else:
            return 0
    elif category == LITTLE_STRAIGHT:
        if dice == [1,2,3,4,5]: #category matches
            return 30
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        if quantity_of_number(dice, repeated_number(dice)[0]) >= 4: #category matches
            return 4 * repeated_number(dice)[0]
        else:
            return 0
    elif category == FULL_HOUSE:
        if len(repeated_number(dice)) > 1:
            if (quantity_of_number(dice, repeated_number(dice)[0]) == 3 and quantity_of_number(dice, repeated_number(dice)[1]) == 2) or (quantity_of_number(dice, repeated_number(dice)[0]) == 2 and quantity_of_number(dice, repeated_number(dice)[1]) == 3):
                return sum(dice)
            else:
                return 0
        else:
            return 0
    elif category == SIXES:
        return quantity_of_number(dice, 6) * 6
    elif category == FIVES:
        return quantity_of_number(dice, 5) * 5
    elif category == FOURS:
        return quantity_of_number(dice, 4) * 4
    elif category == THREES:
        return quantity_of_number(dice, 3) * 3
    elif category == TWOS:
        return quantity_of_number(dice, 2) * 2
    elif category == ONES:
        return quantity_of_number(dice, 1) * 1
    else:
        return 0

    
def repeated_number(dice: list) -> list:
    """
    Returns the repeated number, returns zero if no repeating

    :parameter: dice: list - list with dice rolls
    :return: list - the repeated numbers or zero
    """

    repeated_numbers: list = []
    #check repeated
    for d in [1,2,3,4,5,6]:
        if dice.count(d) > 1:
            repeated_numbers.append(d)
    
    if len(repeated_numbers):
        return repeated_numbers
    else:
        return [0]

def quantity_of_number(dice: list, number: int) -> int:
    """
    Returns the times the given number is repeated

    :parameter: dice: list - list with dice rolls
    :parameter: number: int - number to search for
    :return: int - times the searched number is repeated
    """

    quantity = 0 #initial quantity
    #count
    for d in dice:
        if d == number:
            quantity += 1
    
    return quantity