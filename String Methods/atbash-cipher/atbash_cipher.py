"""
This module contains function to work with atbash cipher
"""

# Auxiliary variables
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
CIPHERED_ALPHABET = "".join(list(reversed(ALPHABET)))

def encode(plain_text: str) -> str:
    """
    Given a text, will encode it with atbash cipher

    plain_text: str - text to encode
    return: str - encoded text
    """

    # Filtering unnecesary chars
    plain_text = plain_text.lower() # all lowercase
    plain_text = "".join(list(filter(lambda c: ALPHABET.find(c) != -1 or NUMBERS.find(c) != -1, plain_text))) # remove punctuation and spaces

    print("Filtered text: ", plain_text)

    # Encoding
    encoded_text = [ CIPHERED_ALPHABET[ALPHABET.index(c)] if c in ALPHABET else c for c in plain_text ]
    # Separate every 5
    encoded_text = ["".join(encoded_text[x:x+5]) for x in range(0, len(encoded_text), 5)]
    print("Encoded text: ", encoded_text)

    return " ".join(encoded_text)


def decode(ciphered_text: str) -> str:
    """
    Given an encoded text, will decode it with atbash cipher

    ciphered_text: str - text to decode
    return: str - decoded text
    """
    
    # Delete spaces
    ciphered_text = ciphered_text.replace(" ","")

    return "".join([CIPHERED_ALPHABET[ALPHABET.index(c)] if str(c) in ALPHABET else c for c in ciphered_text])