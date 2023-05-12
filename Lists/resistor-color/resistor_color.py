"""
This modules contains function related to resistors color coding
"""

def color_code(color: str) -> int:
    """
    Given a color, will return its value

    color: str - color to convert
    return: int - code of provided color
    """
    
    cs = colors()

    return cs.index(color)


def colors() -> list:
    """
    Gives a list with each pair of colors and values

    return: list - the list with pairs
    """

    colors = ["Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Grey","White"]

    return list(map(lambda c: c.lower(),colors))