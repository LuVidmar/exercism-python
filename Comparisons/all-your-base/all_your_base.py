"""
Module with function destined to rebase numbers
"""

def rebase(input_base: int, digits: list, output_base: int) -> list:
    """
    This function rebases a given number with its old base and new base

    input_base: int - base of provided digits
    digits: list - digits to convert
    output_base: int - base to convert digits to
    return: list - converted digits to new base
    """
    
    # Checks
    if not input_base >= 2:
        raise ValueError("input base must be >= 2")
    if not all( 0 <= d < input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if not output_base >= 2:
        raise ValueError("output base must be >= 2")
    if all ( d == 0 for d in digits):
        return [0]
    
    # Calculate number
    number = 0
    for idx, d in enumerate(reversed(digits)):
        number += d * (input_base ** idx)

    print(f"Number in base 10: {number}")

    # Calculate in new base
    new_digits: list = []
    while True: # First we add all reminders
        reminder = number % output_base
        number = int(number / output_base)
        new_digits.insert(0,reminder)

        if number < output_base:
            break
    new_digits.insert(0,number) # At the end we add the number that is less than the output base

    # Cleanup zeros on the left

    if str(new_digits).find("0") == 1:
        new_digits.pop(0)

    return new_digits