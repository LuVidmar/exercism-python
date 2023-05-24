"""
This module contains functions to manipulate rail encoding
"""

def encode(message: str, rails: int) -> str:
    """
    Given a message and the number of rails, will return the encoded message

    message: str - message to encode
    rails: int - number of rails
    return: str - encoded message
    """

    rail_counter = 1
    char_counter = 0
    direction = -1 # 1 goes down, -1 goes up
    rail_array = []
    # add rails to array
    for r in range(rails):
        rail_array.append([])

    # start encoding
    while char_counter < len(message):
        rail_counter += direction
        # if we are in the first or last rail, we invert the direction
        if rail_counter == 0 or rail_counter == rails - 1: 
            direction *= -1
        
        # add letter to rail
        rail_array[rail_counter].append(message[char_counter])

        char_counter += 1

    encoded = ""
    for rail in rail_array:
        encoded += "".join(rail)

    return encoded


def decode(encoded_message: str, rails: int) -> str:
    """
    Given a message and the number of rails, will return the decoded message

    message: str - message to decode
    rails: int - number of rails
    return: str - decoded message
    """

    rail_counter = 1
    char_counter = 0
    direction = -1 # 1 goes down, -1 goes up
    rail_array = []
    # add rails to array
    for r in range(rails):
        rail_array.append([])

    # Create empty rails
    while char_counter < len(encoded_message):
        rail_counter += direction
        # if we are in the first or last rail, we invert the direction
        if rail_counter == 0 or rail_counter == rails - 1: 
            direction *= -1
        
        # add - to rail
        rail_array[rail_counter].append("-")

        char_counter += 1

    # Fill rails with data
    index = 0
    for j, rail in enumerate(rail_array):
        rail_array[j] = encoded_message[index:index+len(rail)]
        index += len(rail)

    # Convert into matrix
    rail_array = [list(rail) for rail in rail_array]

    # Decode
    decoded = ""
    rail_counter = 1
    char_counter = 0
    direction = -1 # 1 goes down, -1 goes up

    while char_counter < len(encoded_message):
        rail_counter += direction
        # if we are in the first or last rail, we invert the direction
        if rail_counter == 0 or rail_counter == rails - 1: 
            direction *= -1
        
        # add letter to decode
        decoded += rail_array[rail_counter].pop(0)

        char_counter += 1

    return decoded