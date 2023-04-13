"""
This module contains functions to resolve square problems.
"""
def square(number: int):
    """
    Returns number of grains in given square.

    :argument: int - number of square
    :return: int - number of grains in square
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    return 2 ** (number-1)

NUMBER_OF_SQUARES = 64
def total():
    """
    Returns the total number of grains in the whole board.

    :return: int - total number of grains
    """
    total = 0
    for i in range(NUMBER_OF_SQUARES):
        total = total + 2 ** i
    return total
