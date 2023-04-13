"""Lasagna related functions

This module has functions to calculate preparation and baking times for lasagna.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the remaining time.

    :param elapsed_bake_time: int = the time that has passed.
    :return: int - the time remaining.

    This function takes one integer representing the time that has passed and returns the time remaining to bake.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


PREPARATION_TIME = 2

def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers in lasagna.
    :return: int - time it will take to preparate.

    This function takes an integer representing the number of layers in the lasagna and returns the
    time that it will take to preparate.
    """

    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time