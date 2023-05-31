"""
This module contains a function to make diamond letters
"""

ABECEDARY = "abcdefghijklmnopqrstuvwxyz"
ABECEDARY_AS_LIST = list(ABECEDARY.upper())

def rows(letter: str) -> str:
    """
    Given a letter, will mike a nice diamond

    letter: str - letter to base the diamond
    return: str - diamond
    """

    # Calculate some variables
    height = ABECEDARY_AS_LIST.index(letter) * 2 + 1 # also width
    matrix = [ [ '-' for i in range(height) ] for j in range(height) ] # Empty matrix to use
    print(matrix)

    # Start printing
    space_sides = int(height / 2)
    direction = 1 # 1 down, -1 up
    for idx, line in enumerate(matrix):
        
        # Contemplate start, end and middle
        if space_sides == -1: # reached middle
            space_sides = 1
            direction = -1

        space_middle = height - space_sides * 2 - 2
        letter_idx = idx if direction == 1 else height - idx - 1

        if idx == 0 or idx == len(line) - 1: # start and end
            matrix[idx] = [ " " for i in range(space_sides) ] + [ABECEDARY_AS_LIST[letter_idx]] + [ " " for i in range(space_sides) ]
        else: # every other case
            matrix[idx] = [ " " for i in range(space_sides) ] + [ABECEDARY_AS_LIST[letter_idx]] + [ " " for i in range(space_middle) ] + [ABECEDARY_AS_LIST[letter_idx]] + [ " " for i in range(space_sides) ]
        
        space_sides -= 1 * direction

    matrix = [ "".join(m) for m in matrix ]
    print("\n".join(matrix))
    return matrix