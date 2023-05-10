"""
This module contains a function that determines weather a word is an isogram or not
"""

def is_isogram(string: str) -> bool:
    """
    Determines if given string is isogram

    string: str - string to analize
    return: bool - True if isogram, false if not
    """

    # Firstly normalize input
    string = string.lower().replace(" ","").replace("-","")

    used_chars = "" #empty string

    # Lets analize each character in string
    for c in string:
        if used_chars.find(c) == -1: 
            used_chars += c # if character wasnt already used, add it
        else:
            return False # otherwise repeated, not isogram
        
    return True # Never returned false, then its isogram