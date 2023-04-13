"""
This module contains only one function related to the collatz conjecture
"""
def steps(number: int) -> int:
    """
    Returns the number of steps necessaries to satisfy collatz conjecture

    :argument number: int - number to process
    :return: int - number of steps necessaries
    """
    #validate number
    if (number < 1):
        raise ValueError("Only positive integers are allowed")
    
    #start calculating
    n: int = number
    steps = 0
    #operate until n is 1
    while(n != 1):
        steps += 1 #add one step each time
        #two cases, odd and even
        if(n % 2 != 0): #odd number
            n = n * 3 + 1 #3n+1
        else:
            n = n/2 #n/2

    return steps