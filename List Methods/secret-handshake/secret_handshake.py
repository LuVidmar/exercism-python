"""
This module contains the secrest of the handshake
"""

def commands(binary_str: str) -> list:
    """
    Given the binary string of a number between 1 and 31, will give you the corresponding action

    binary_str: str - number in binary chosen
    return: list - actions to take
    """

    print(binary_str)
    digits = list(binary_str)
    
    actions = []
    
    if digits[-1] == "1":
        actions.append("wink")
    if digits[-2] == "1":
        actions.append("double blink")
    if digits[-3] == "1":
        actions.append("close your eyes")
    if digits[-4] == "1":
        actions.append("jump")
    if digits[-5] == "1":
        actions.reverse()

    return actions