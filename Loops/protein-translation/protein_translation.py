"""
This module has a function to translate ARN into proteins
"""

def proteins(strand: str) -> list:
    """
    Given a strand of RNA, will translate it into its composing codons

    strand: str - strand to analize
    return: list - list of codons
    """

    CODE = [
        [["AUG"], "Methionine"],
        [["UUU", "UUC"], "Phenylalanine"],
        [["UUA", "UUG"], "Leucine"],
        [["UCU", "UCC", "UCA", "UCG"], "Serine"],
        [["UAU", "UAC"], "Tyrosine"],
        [["UGU", "UGC"], "Cysteine"],
        [["UGG"], "Tryptophan"],
        [["UAA", "UAG", "UGA"], "STOP"]
    ]

    # First we divide in codons
    codons = [ strand[idx:idx+3] for idx in range(0,len(strand),3) ]

    # Translate each codon
    translated = []
    for codon in codons:
        for codes in CODE:
            if codon in codes[0]:
                if codes[1] == "STOP":
                    return translated
                else:
                    translated.append(codes[1])

    return translated