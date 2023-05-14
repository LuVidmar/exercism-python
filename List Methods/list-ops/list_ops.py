"""
Implementation of list methods
"""

def append(list1: list, list2: list) -> list:
    """
    Given two lists, add all items in the second list to the end of the first list

    list1, list2: list - lists to append
    return: list - appended lists
    """
    
    return list1 + list2


def concat(lists: list) -> list:
    """
    Given a series of lists, combine all items in all lists into one flattened list

    lists: list - lists of lists
    return: list - plain list with all elements
    """
    
    concat = []
    for lst in lists:
        concat += lst

    return concat


def filter(function, list: list) -> list:
    """
    Given a predicate and a list, return the list of all items for which predicate(item) is True

    function: function - call with item, returns True or False
    list: list - items to filter
    return: list - filtered list
    """
    
    items = []
    for l in list:
        if function(l):
            items = concat([items,[l]])
    
    return items


def length(list: list) -> int:
    """
    Given a list, return the total number of items within it

    list: list - items to count
    return: int - count total
    """

    count = 0
    for l in list:
        count += 1
    
    return count


def map(function, list: list) -> list:
    """
    Given a function and a list, return the list of the results of applying function(item) on all items

    function: function - process to apply to all items
    list: list - items to process
    return: list - proccessed items
    """
    
    items = []
    for l in list:
        items = concat([items,[function(l)]])

    return items


def foldl(function, list: list, initial: any) -> any:
    """
    Given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the left using function(accumulator, item)
    
    function: function - apply to every item
    list: list - list of items to apply the function to
    initial: any - accumulator
    return: any - accumulator at the end
    """

    for l in list:
        initial = function(initial, l)

    return initial

def foldr(function, list: list, initial: any) -> any:
    """
    Given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right using function(accumulator, item)

    function: function - apply to every item
    list: list - list of items to apply the function to
    initial: any - accumulator
    return: any - accumulator at the end
    """

    return foldl(function, reverse(list), initial)


def reverse(list: list) -> list:
    """
    Given a list, return a list with all the original items, but in reversed order

    list: list - items to reverse
    return: list - reversed list
    """

    items = []
    for idx in range(length(list)):
        items = concat([items,[list[-(idx+1)]]])

    return items