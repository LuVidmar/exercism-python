"""
This module has functions related to sum of squares and square of sums
"""

def square_of_sum(number: int) -> int:
    """
    Calculates the square of a sum.

    :argument number: int - the number up to which the square of sum will be calculated
    :return: int - squared sum
    """
    int_sum = 0
    #calculate sum
    for n in range(number + 1):
        int_sum += n
    
    return int_sum ** 2 #return squared sum


def sum_of_squares(number: int) -> int:
    """
    Calculates the sum of squares

    :argument: int - the number up to which the sum of squares will be calculated
    :return: int - sum of squares
    """

    sum_of_squares = 0
    #calculate all at once
    for n in range(number + 1):
        sum_of_squares += n**2
    
    return sum_of_squares


def difference_of_squares(number: int) -> int:
    """
    Calculates the difference between the sum of squares and the squared sum

    :argument: int - the number up to which the difference will be calculated
    :return: int - difference between the two operations
    """
    return square_of_sum(number) - sum_of_squares(number)
