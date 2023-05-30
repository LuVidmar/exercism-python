"""
Module to convert numbers from arabic to roman.
"""

def roman(number: int) -> str:
    """
    Given the number, will convert it into roman notation

    number: int - number in decimal notation
    return: str - equivalent roman number
    """

    # Validation
    if number > 3999 or number < 0:
        raise ValueError("out of range")
    
    # Divided
    thousands = int(number / 1000)
    number -= thousands * 1000
    hundreds = int(number / 100)
    number -= hundreds * 100
    tens = int(number / 10)
    number -= tens * 10
    units = number
    digits = [(thousands,"M","-","-"), (hundreds,"C","D","M"), (tens,"X","L","C"), (units,"I","V","X")]

    # Convert
    converted = ""
    for digit in digits:
        if 1 <= digit[0] <= 3:
            converted += "".join([ digit[1] for i in range(digit[0]) ])
        elif 4 == digit[0]:
            converted += digit[1] + digit[2]
        elif 5 == digit[0]:
            converted += digit[2]
        elif 6 <= digit[0] <= 8:
            converted += digit[2] + "".join([ digit[1] for i in range(digit[0] - 5) ])
        elif 9 == digit[0]:
            converted += digit[1] + digit[3]
        elif 10 == digit[0]:
            converted += digit[3]

    return converted