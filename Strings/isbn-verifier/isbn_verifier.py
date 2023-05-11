"""
This module includes only one function to determine valid isbns
"""

def is_valid(isbn: str) -> bool:
    """
    Function that recieves isbn as string and determines validity

    isbn: str - isbn code to analize
    return: bool - True if valid isbn was supplied
    """

    isbn_valid = "1234567890X" # used to validate
    isbn = isbn.upper().replace("-","") # normalize

    # Initial checks
    if any( isbn_valid.find(c) == -1 for c in isbn): #All digits are valid
        return False
    if len(isbn) != 10: # has len 10
        return False
    if isbn.find("X") != 9 and isbn.find("X") != -1: # X only at the end
        return False

    isbn_list = list(isbn) #auxiliary list

    # Modify string
    print(isbn_list)
    isbn_list = [10 if c == "X" else c for c in isbn_list] # Replace X with 10
    print(isbn_list)

    isbn_list = [int(c) for c in isbn_list]

    print (isbn_list)
    # Calculate formula
    sum = 0
    for idx, n in enumerate(isbn_list):
        sum += n * (10 - idx)
    # Return
    return sum % 11 == 0
        