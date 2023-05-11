"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def sublist(list_one: list, list_two: list) -> int:
    """
    This functions determines weather list one is a sublist, superlist, equal or unequal to list two

    list_one, list_two: list(int) - lists to analize
    return: int - code for classification
    """

    # Easier to work with strings (ending character to avoid 2 equaling 22)
    one = "".join(str(list_one)).replace(" ","").replace("[","").replace("]","").lstrip().rstrip()+","
    two = "".join(str(list_two)).replace(" ","").replace("[","").replace("]","").lstrip().rstrip()+","

    if one == two:
        return EQUAL
    elif one.find(two) != -1: # one contains two -> one SUPERLIST of two
        return SUPERLIST
    elif two.find(one) != -1: # two contains one -> one SUBLIST of two
        return SUBLIST
    else:
        return UNEQUAL