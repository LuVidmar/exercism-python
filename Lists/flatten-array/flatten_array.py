"""
This module contains a function to flaten arrays
"""

def flatten(list_to_flatten: list) -> list:
    """
    Given a list, will flatten it

    list_to_flatten: list - list to flatten
    return: list - flattened list 
    """

    print("--------")
    flattened = []
    for item in list_to_flatten: # analize every item
        print(f"analizing {item}")
        if type(item) is list: # if it is a sublist, we use recursivity
            item = flatten(item)
            flattened.extend(item) # add flattened sublist
        else:
            flattened.append(item) # it is not a list, we just add it
    print(f"flattened {flattened}")

    # Now we are ready to filter what we dont need
    flattened = [ item for item in flattened if item != None ]
    return flattened