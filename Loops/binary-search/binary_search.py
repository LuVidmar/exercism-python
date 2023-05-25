"""
This module contains a function to do binary search
"""

def find(search_list: list, value: int) -> int:
    """
    Given a list and the value to search for, will return the number of iterations needed to find

    search_list: list - where to find value
    value: int - value to seach for
    return: int - number of iterations
    """

    # Variables to use
    index = 0
    direction = 1 # right 1, left -1
    sl = search_list

    # Take middle value and check wether its bigger or smaller
    while True:

        if len(sl) == 0:
            raise ValueError("value not in array")

        middle = int(len(sl)/2)
        index += (middle + 1) * direction
        if value == sl[middle]: # found element
            break
        elif value > sl[middle]: # bigger than element
            sl = sl[middle+1:]
            direction = 1
        else: # smaller than element
            sl = sl[:middle]
            direction = -1
        
    if not len(search_list) % 2:
        return index
    else:
        return index -1