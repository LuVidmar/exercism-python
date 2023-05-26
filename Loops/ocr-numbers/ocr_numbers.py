"""
This module contains functions to OCR numbers
"""

OCR_NUMBERS = {
    "0": [
        " _ ",
        "| |",
        "|_|",
        "   "
    ],
    "1": [
        "   ",
        "  |",
        "  |",
        "   "
    ],
    "2": [
        " _ ",
        " _|",
        "|_ ",
        "   "
    ],
    "3": [
        " _ ",
        " _|",
        " _|",
        "   "
    ],
    "4": [
        "   ",
        "|_|",
        "  |",
        "   "
    ],
    "5": [
        " _ ",
        "|_ ",
        " _|",
        "   "
    ],
    "6": [
        " _ ",
        "|_ ",
        "|_|",
        "   "
    ],
    "7": [
        " _ ",
        "  |",
        "  |",
        "   "
    ],
    "8": [
        " _ ",
        "|_|",
        "|_|",
        "   "
    ],
    "9": [
        " _ ",
        "|_|",
        " _|",
        "   "
    ]
}


def convert(input_grid: list) -> str:
    """
    Given a matrix of multiple lines of characters, will try to OCR

    input_grid: list - matrix of chars
    return: str - OCR recognized chars
    """

    # Convert into matrix
    matrix = []
    for line in input_grid:
        matrix.append(list(line))

    print(matrix)

    # Basic validations
    if len(matrix) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for line in matrix:
        if len(line) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
        
    # Separate in lines
    number_of_lines = int(len(matrix) / 4)
    lines = [ matrix[i:i+4] for i in range(0,len(matrix),4) ]

    # Process every line
    processed = list(map(_convert,lines))
    
    return ",".join(processed)
    
   
def _convert(matrix) -> str:
    """
    Given a matrix of a signle lines of characters, will try to OCR

    input_grid: list - matrix of chars in one line
    return: str - OCR recognized chars
    """

    # Create empty number list
    numbers = []
    quant_of_numbers = len(matrix[0]) / 3
    numbers = [ [] for n in range(int(quant_of_numbers)) ]

    # Fill number list
    for line in matrix:
        idx = 0
        j = 0
        while idx < len(line):
            numbers[j].append(line[idx:idx+3])
            idx += 3
            j += 1

    # Convert into strings
    for i, number in enumerate(numbers):
        for j, line in enumerate(number):
            numbers[i][j] = "".join(line)


    # Search for number in database
    converted = ""
    OCR_VALUES = list(OCR_NUMBERS.values())
    for n in numbers:
        index = -1
        # Find the index of the number
        for i, number in enumerate(OCR_VALUES):
            if number == n: # found
                index = i
                break
        if index != -1: # not found
            converted += list(OCR_NUMBERS.keys())[index]
        else:
            converted += "?"

    print(numbers)
    return converted


convert(
    [
        "    _  _ ",
        "  | _| _|",
        "  ||_  _|",
        "         ",
        "    _  _ ",
        "|_||_ |_ ",
        "  | _||_|",
        "         ",
        " _  _  _ ",
        "  ||_||_|",
        "  ||_| _|",
        "         ",
    ]
)
"123,456,789"

convert(
    [
        "    _  _     _  _  _  _  _  _ ",
        "  | _| _||_||_ |_   ||_||_|| |",
        "  ||_  _|  | _||_|  ||_| _||_|",
        "                              ",
    ]
)
"1234567890"
convert(
    [
        "       _     _           _ ",
        "  |  || |  || |     || || |",
        "  |  | _|  ||_|  |  ||_||_|",
        "                           ",
    ]
)
"11?10?1?0"