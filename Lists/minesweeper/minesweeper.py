"""
This module contains a function to determine minesweep values
"""

def annotate(minefield: list) -> list:
    """
    Given a board, will return the same board with its corresponding values

    minefield: list - matrix with board
    return: list - solved board
    """

    # Validate board
    lines_have_same_len = all([ len(line) == len(minefield[0]) for line in minefield ])
    if not lines_have_same_len:
        raise ValueError("The board is invalid with current input.")

    # Info
    minefield = [ line.replace(" ","-") for line in minefield] # replacing space to make counting easier
    print('\n'.join(minefield))

    # Determine values
    values = [ list(line) for line in minefield ] # empty matrix to fill with values
    for j, line in enumerate(minefield):
        for i, mine in enumerate(line):
            print(f"{i},{j}: {mine}")

            # Check if it is a mine
            if minefield[j][i] == '*':
                print("Its a mine!")
                continue
            elif minefield[j][i] != '-': # Check for invalid chars
                raise ValueError("The board is invalid with current input.")
            
            # Not a mine, count
            count = 0
            space_to_left = i - 1 >= 0
            space_to_right = i + 1 < len(line)
            space_up = j - 1 >= 0
            space_below = j + 1 < len(minefield)
            print(f"left: {space_to_left}, right: {space_to_right}, up: {space_up}, below: {space_below}")
            # Count
            if space_to_left:
                count += 1 if minefield[j][i-1] == '*' else 0 # left
                if space_up:
                    count += 1 if minefield[j-1][i-1] == '*' else 0 # left, up
                if space_below:
                    count += 1 if minefield[j+1][i-1] == '*' else 0 # left, below
            if space_to_right:
                count += 1 if minefield[j][i+1] == '*' else 0 # right
                if space_up:
                    count += 1 if minefield[j-1][i+1] == '*' else 0 # right, up
                if space_below:
                    count += 1 if minefield[j+1][i+1] == '*' else 0 # right, below
            if space_up:
                count += 1 if minefield[j-1][i] == '*' else 0 # up
            if space_below:
                count += 1 if minefield[j+1][i] == '*' else 0 # below

            print(f"Counted: {count}")
            values[j][i] = str(count)

    values = [ "".join(val).replace("0"," ") for val in values ]
    print("\n".join(values))
    return values


annotate(["     ", "   * ", "     ", "     ", " *   "])