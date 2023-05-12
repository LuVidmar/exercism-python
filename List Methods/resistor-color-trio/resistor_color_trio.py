"""
This module contains a funciton to work with 3 lines resistors
"""

def label(colors: list) -> int:
    """
    Given a list of 3 colors, will translate it to its ohmic value

    colors: list - 3 colors
    return: int - resistance
    """

    # Auxiliary lists
    color_codes = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"] #auxilary list

    # Value calculation
    value = color_codes.index(colors[0]) * 10 + color_codes.index(colors[1])
    value *= 10 ** color_codes.index(colors[2])

    # Unit computation
    unit = ""
    if value >= 10 ** 9:
        value /= 10 ** 9
        unit = "giga"
    elif value >= 10 ** 6:
        value /= 10 ** 6
        unit = "mega"
    elif value >= 10 ** 3:
        value /= 10 ** 3
        unit = "kilo"
    
    unit += "ohms"
    

    return str(int(value)) + " " + unit