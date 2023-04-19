"""
Module that contains one function that interprets raindrops.
"""

def convert(number: int) -> str:
    """
    number: int - number to analize
    return: str - the raindrops
    """

    response: str = ""
    if number % 3 == 0: #is a factor of 3
        response += "Pling"
    if number % 5 == 0: #is a factor of 5
        response += "Plang"
    if number % 7 == 0: #is a factor of 7
        response += "Plong"
    if response == "":
        response = str(number)
    
    return response