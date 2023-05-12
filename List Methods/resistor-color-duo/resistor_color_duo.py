"""
This module contains a functio to help determine coded color resistors
"""

def value(colors: list) -> int:
    """
    Given a list of colors, this function will convert them to values

    colors: list - this list will contain the colors of the resistor
    return: int - the value of the provided colors
    """

    color_codes = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"] #auxilary list'

    value = 0
    for idx, color in enumerate(colors):
        if idx >= 2:
            break
            
        value += color_codes.index(color) * (10 ** (1 - idx))

    return value