"""
This module contains a function to calculate the square root
"""

def square_root(number: int) -> float:
    """
    Calculates the square root

    number: int - number to calculate the square root of
    return: float - square root
    """
    
    i = 0
    number *= 100 * 100 # moved two decimals

    # Determine integer
    while True:
        if number == i * i:
            break
        i += 1

    sqrt = ".".join([str(i)[:-2],str(i)[-2:]])
    print(sqrt)
    
    return float(sqrt)