"""
This module cointains a function to caesar cipher
"""

def rotate(text: str, key: int) -> str:
    """
    Takes a string and key and returns the ciphered string

    text: str - text to cypher
    key: int - number of times to rotate
    return: str - ciphered text
    """
    
    abecedary = "abcdefghijklmnopqrstuvwxyz" # Auxiliary string
    abecedary_caps = abecedary.upper()

    words = list(text)

    for idx, c in enumerate(words):
        if abecedary.find(c) != -1: #its lowercase
            i = abecedary.index(c)
            words[idx] = abecedary[i + key] if i + key < len(abecedary) else abecedary[i + key - len(abecedary)]
        elif abecedary_caps.find(c) != -1: #its uppercase
            i = abecedary_caps.index(c)
            words[idx] = abecedary_caps[i + key] if i + key < len(abecedary_caps) else abecedary_caps[i + key - len(abecedary_caps)]

    return "".join(words)