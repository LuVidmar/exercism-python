"""
This module contains the functions needed to encode and decode in 7bits VLQ
"""

def encode(numbers: list) -> list:
    """
    Given a list of numbers, will encode them into VLQ

    numbers: list - numbers to encode
    return: list - encoded numbers
    """
    
    encoded_numbers = [] # will convert each number and store it here

    for number in numbers:

        # Firstly we create a list in binary
        binary_number = bin(number)
        binary_number = list(binary_number.removeprefix("0b"))

        # We separate in sub lists of 7 bits
        SEPARATION = 7
        separated_in_7 = [ list(reversed(binary_number))[i:i+SEPARATION] for i in range(0,len(binary_number),SEPARATION) ]
        separated_in_7 = [ list(reversed(s)) for s in separated_in_7 ]
        separated_in_7.reverse() # Bring it back

        # Normalize (add ceros where we have less than 7 bits)
        for idx, s in enumerate(separated_in_7):
            while len(separated_in_7[idx]) < SEPARATION:
                separated_in_7[idx].insert(0,'0')

        # Add 1 in every byte at start except for last
        separated_in_8 = []
        for idx, s in enumerate(separated_in_7):
            if separated_in_7.index(s) == (len(separated_in_7) - 1):
                s.insert(0,'0')
            else:
                s.insert(0,'1')
            separated_in_8.append(s) 

        # Convert to one string
        encoded_bytes = []
        for s in separated_in_8:
            encoded_bytes.append(int("".join(s),2))

        encoded_numbers.extend(encoded_bytes)

    return encoded_numbers


def decode(bytes_: list) -> list:
    """
    Given a list of numbers, will decode them

    numbers: list - numbers to decode
    return: list - decoded numbers
    """
    
    # For each byte, conver to binary
    bytes_as_bin = []
    for byte in bytes_:
        bytes_as_bin.append(list(bin(byte).removeprefix("0b")))

    print(bytes_as_bin)
    # Normalize (every number has to have 8 bit)
    BITS = 8
    for idx, byte in enumerate(bytes_as_bin):
        while len(bytes_as_bin[idx]) < BITS:
            bytes_as_bin[idx].insert(0,'0') # fill with zeros

    print(bytes_as_bin)
    # Separate numbers with 1 at the start
    numbers = []
    b = []
    has_ending = False
    for byte in bytes_as_bin:
        if byte[0] == '1': # not last byte in number
            b.append(byte[1:])
        else: # last byte in number
            b.append(byte[1:]) # we add last byte
            numbers.append(b)
            b = [] # set up for next number
            has_ending = True

    # Incomlete sequence
    if not has_ending:
        raise ValueError("incomplete sequence")
    
    # Format it
    print(numbers)
    decoded = []
    for number in numbers:
        number_in_bin = ""
        for bytes in number:
            number_in_bin += "".join(bytes)
        decoded.append(int(number_in_bin,2))

    print(decoded)
    return decoded