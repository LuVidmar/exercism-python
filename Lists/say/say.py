"""
Module that contains a function to convert numbers to readable english
"""

BILLION = 1000000000
MILLION = 1000000
THOUSAND = 1000
HUNDRED = 100
TEN = 10

NUMBERS = ["zero", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ",
           "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
TENS = ["-","-","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def say(number: int) -> str:
    """
    Given a number, will make it readable

    number: int - number to convert
    return: str - readable number in english
    """

    # Validations
    if number == 0:
        return NUMBERS[0]
    elif not (0 < number < 999999999999):
        raise ValueError("input out of range")
    
    converted = _say(number)

    # Cleanup
    converted = converted.strip()
    print(converted)
    
    return converted
    

def _say(number: int) -> str:

    divisions = {}
    # Divide
    divisions["billions"] = int(number / BILLION)
    number -= divisions["billions"] * BILLION
    divisions["millions"] = int(number / MILLION)
    number -= divisions["millions"] * MILLION
    divisions["thousands"] = int(number / THOUSAND)
    number -= divisions["thousands"] * THOUSAND
    divisions["hundred"] = int(number / HUNDRED)
    number -= divisions["hundred"] * HUNDRED
    divisions["tens"] = int(number / TEN)
    number -= divisions["tens"] * TEN

    converted = ""
    # Conversion
    if divisions["billions"] != 0:
        converted += _say(divisions["billions"]) + "billion "
    if divisions["millions"] != 0:
        converted += _say(divisions["millions"]) + "million "
    if divisions["thousands"] != 0:
        converted += _say(divisions["thousands"]) + "thousand "
    if divisions["hundred"] != 0:
        converted += _say(divisions["hundred"]) + "hundred "
    if divisions["tens"] > 1:
        converted += TENS[divisions["tens"]] + "-"
    if number != 0:
        if divisions["tens"] == 1:
            number += 10
        converted += NUMBERS[number]

    # Cleanup
    converted = converted.removesuffix("-")
    converted = converted.removeprefix("-")

    return converted