"""
This module contains a function to transpose matrixes.
"""

def transpose(lines: str) -> str:
    """
    Given a matrix, will transpose it

    lines: str - matrix as a string
    return: str - transposed matrix as a string
    """

    # Preprocessing
    rows = lines.split("\n")
    print(f"1. rows: {rows}")
    
    # 1 2 3
    # 4   5
    #   6 7

    # Calculate maxs
    max_height = max(len(row) for row in rows)
    print(f"max_height: {max_height}")

    # Add needed identation
    for idx, row in enumerate(rows):
        if len(row) < max_height:
            rows[idx] = row + "".join([ "-" for i in range(max_height - len(row)) ])

    print(f"2. rows: {rows}")

    # Transposing
    transposed = []
    index = 0
    while index < max_height:
        line = []
        for row in rows:
            if index < len(row):
                line.append(row[index])
        transposed.append(line)
        index += 1

    print(f"transposed: {transposed}")

    # Make it readable
    transposed = list(map(lambda l: "".join(l).rstrip("-"),transposed))
    print(f"transposed: {transposed}")
    transposed = list(map(lambda l: l.replace("-"," "),transposed))
    print(f"transposed: {transposed}")
    transposed = "\n".join(transposed)
    print("matrix:")
    print(transposed)
    
    return transposed