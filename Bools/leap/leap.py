"""
This module only contains a function to determine leap years
"""

def leap_year(year: int) -> bool:
    """
    Determines weather its a leap year

    :argument year: int - year to analyze
    :return: bool
    """
    if year % 400 == 0:
        return True
    elif (year % 4 == 0 and not year % 100 == 0):
        return True
    else:
        return False