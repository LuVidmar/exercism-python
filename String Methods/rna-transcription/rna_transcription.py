"""
This module contains a function to work with DNA and RNA
"""

def to_rna(dna_strand: str) -> str:
    """
    Given a DNA sequence, will return its complementary RNA
    """

    # Auxiliary strings
    dna = "ACGT"
    rna = "ACGU"

    return "".join([ rna[-(1+dna.index(d))] for d in dna_strand])