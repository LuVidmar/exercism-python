"""
This module contains a function to determine formatting of parenthesis, braces and brackets
"""

def is_paired(input_string: str) -> bool:
    """
    Function determines if parenthesis, braces and brackets are formatted correctly

    input_string: str - string to analize
    return: bool - True if correctly formatted
    """

    opening_chars = ["(","[","{"]
    closing_chars = [")","]","}"]

    saved_chars = []

    # Counts
    level = 0

    for c in input_string:
        print(c)
        # At any given moment level must not be negative
        if level < 0:
            return False
        
        # Analize
        if c in opening_chars: # Add level and save char
            level += 1
            saved_chars.append(c)
        elif c in closing_chars: # Remove level and remove from saved
            if len(saved_chars) != 0: 
                level -= 1
                if saved_chars.pop() != opening_chars[closing_chars.index(c)]: # Closing char must correlated with latest opening char
                    return False
            else:
                return False
        print(f"level: {level} | savedchars: {saved_chars}")
            
    return level == 0 # Level must be zero (all openings have closures)