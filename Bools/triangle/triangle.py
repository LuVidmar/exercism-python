"""
This module contains functions to determine the type of triangle
"""

def equilateral(sides):
    """
    Checks if triangle is equilateral
    
    :argument: sides - sides of the triangle
    :return: boolean - weather the triangle is equilateral
    """
    
    # First check initial conditions
    if (not initial_conditions(sides)):
        return False
    
    a, b, c = sides

    #actual determination
    if a == b and b == c:
        return True
    else:
        return False
    

def isosceles(sides):
    """
    Checks if triangle is isosceles
    
    :argument: sides - sides of the triangle
    :return: boolean - weather the triangle is isosceles
    """
    # First check initial conditions
    if (not initial_conditions(sides)):
        return False
    
    a, b, c = sides

    #actual determination
    if a == b or a == c or b == c and not equilateral(sides):
        return True
    else:
        return False


def scalene(sides):
    """
    Checks if triangle is scalene
    
    :argument: sides - sides of the triangle
    :return: boolean - weather the triangle is scalene
    """
    # First check initial conditions
    if (not initial_conditions(sides)):
        return False
    
    a, b, c = sides

    #actual determination
    if a != b and a != c and b != c:
        return True
    else:
        return False

def initial_conditions(sides):
    """
    Makes all necessary validations for any sides

    :argument: sides - sides to check
    :return: boolean - weather sides are correct
    """

    #check length of each side
    a, b, c = sides
    for side in sides:
        if not side > 0:
            return False
    #check for lengths of any two sides must be greater than or equal to the length of the third side
    if a + b < c or b + c < a or a + c < b:
        return False

    return True
