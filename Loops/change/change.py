"""
This module contains a function to solve the change problem.
"""

from itertools import combinations_with_replacement

def find_fewest_coins(coins: list, target: int) -> list:
    """
    Given the coins available and the target change, will return you the smallest quantity of coins needed

    coins: list - values of coins available
    target: int - change to reach
    return: list - list of used coins to reach change
    """

    # Logs
    print(f"Coins: {coins}")
    print(f"Target: {target}")

    # Startup
    factors = [ int(target / coin) for coin in coins ]
    coins_to_use = [ coin for idx, coin in enumerate(coins) if factors[idx] != 0 ] # Cleanup zeros

    # Validations (and edge cases)
    if target == 0:
        return []
    elif target < 0:
        raise ValueError("target can't be negative")
    elif any(coin == target for coin in coins):
        return [target]
    elif len(coins_to_use) == 0:
        raise ValueError("can't make target with given coins")


    # Max coins possible (we define it as function to shorten next step if possible)
    max_coins = lambda i: int(target / min(coins_to_use[i:])) + 1
    
    # Find all possible combinations
    possibilities = []
    for i in range(max_coins(-2)): # try with last two
        combinations = combinations_with_replacement(coins_to_use,i)
        for combination in combinations:
            if sum(combination) == target:
                possibilities.append(combination)

    if len(possibilities) == 0:
        for i in range(max_coins(0)): # try with everything
            combinations = combinations_with_replacement(coins_to_use,i)
            for combination in combinations:
                if sum(combination) == target:
                    possibilities.append(combination)

    # More validations
    if len(possibilities) == 0:
        raise ValueError("can't make target with given coins")

    return_list = list([ combination for combination in possibilities if len(combination) == min([ len(combination) for combination in possibilities ])][0])
    return_list.sort()
    return return_list

find_fewest_coins([4, 5], 27)