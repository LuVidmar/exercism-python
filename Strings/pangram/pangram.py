"""
This module contains a function to determine if a string is a panagram.
"""

def is_pangram(sentence: str) -> bool:
    """
    This function determines weather a function is a panagram

    sentence: str - the input sentece to analize
    :return: bool - true if the sentence is a pangram
    """

    abecedary = "abcdefghijklmnopqrstuvwxyz"

    # Format
    sentence = sentence.lower()

    # Split into list of words and remove whitespaces
    sentence_as_list = list(sentence)

    # Check for each letter
    has_each_letter: list(bool) = [False for x in abecedary] #initialize every letter in false
    
    for word in sentence_as_list:
        word = word.rstrip().lstrip() # trim spaces
        for c in word:
            index = abecedary.find(c)
            if index != -1: # letter is in abecedary
                has_each_letter[index] = True
    
    return all(has_each_letter)