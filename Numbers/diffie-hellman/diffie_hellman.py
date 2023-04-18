"""
This module has functions related to the generation of private and public keys with prime numbers.
"""

import secrets


def private_key(p: int) -> int:
    """
    Generate a private key.

    p: int - number upto which the prime number will be generated
    return: int - returns private key
    """

    randNumber: int = 0
    while randNumber < 2:  # rand number between 2 and p
        randNumber = secrets.randbelow(p)

    return randNumber


def public_key(p: int, g: int, private: int) -> int:
    """
    Generate public key using A = g^private mod p

    p: int - number used to genrate key
    g: int - number used to genrate key
    private: int - private key generated before
    return: int - generated public key
    """

    return (g**private) % p


def secret(p: int, public: int, private: int) -> int:
    """
    Generate secret using s = public^private mod p

    p: int - number used to genrate key
    public: int - shared public key
    private: int - private key generated before
    return: int - generated secret
    """

    return (public**private) % p
