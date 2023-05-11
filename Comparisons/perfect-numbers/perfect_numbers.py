"""
This module contains a function that classifies numbers accoording to Nicomachus scheme
"""

def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors: list = []

    # Calculate factors
    for i in range(1,number,1):
        if number % i == 0: # its a factor
            factors.append(i)

    # Sum of factors
    if sum(factors) == number:
        return "perfect"
    elif sum(factors) > number:
        return "abundant"
    else:
        return "deficient"