"""
Lyrics of the song: "The Twelve Days of Christmas."
"""

DAYS = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"]
COMPLETE_VERSE = [
    "twelve Drummers Drumming, ",
    "eleven Pipers Piping, ",
    "ten Lords-a-Leaping, ",
    "nine Ladies Dancing, ",
    "eight Maids-a-Milking, ",
    "seven Swans-a-Swimming, ",
    "six Geese-a-Laying, ",
    "five Gold Rings, ",
    "four Calling Birds, ",
    "three French Hens, ",
    "two Turtle Doves, ",
    "a Partridge in a Pear Tree.",
]

def recite(start_verse: int, end_verse: int) -> list[str]:
    """
    Given a starting and ending verse, will recite

    start_verse: int - starting verse
    end_verse: int - ending verse
    return: list[str] - list with all possible verses
    """

    vs = []
    for i in range(start_verse, end_verse + 1, 1):
        vs.append(verse(i))
    return vs

def verse(end_verse: int) -> str:
    """
    Given a final verse will, recite verse until that verse

    end_verse: int - final verse
    return: str - verse until certain point
    """

    # Add parts of phrase
    verse = list(reversed(COMPLETE_VERSE))[:end_verse]
    verse.reverse()

    # Add 'and'
    if len(verse) > 1:
        verse.insert(-1, "and ")

    # Add start
    verse.insert(0,f"On the {DAYS[end_verse - 1]} day of Christmas my true love gave to me: ")

    print("".join(verse))
    return "".join(verse)