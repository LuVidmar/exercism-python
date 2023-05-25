"""
This module contains a function to get recite the nursery rhyme 'This is the House that Jack Built'.
"""

def recite(start_verse: int, end_verse: int) -> list:
    """
    Given starting and ending verse, will give you all possible combinations
    
    start_verse: int - number to start at
    end_verse: int - number to end at
    return: list - list of combinations
    """

    COMPLETE_VERSE = [
        "This is the horse and the hound and the horn",
        "belonged to the farmer sowing his corn",
        "kept the rooster that crowed in the morn",
        "woke the priest all shaven and shorn",
        "married the man all tattered and torn",
        "kissed the maiden all forlorn",
        "milked the cow with the crumpled horn",
        "tossed the dog",
        "worried the cat",
        "killed the rat",
        "ate the malt",
        "lay in the house that Jack built."
    ]
    
    # Adapt variables
    COMPLETE_VERSE.reverse()
    end_verse += 1

    # Take the part of the verse that was asked for
    i = start_verse
    verses = []
    while i < end_verse:
        verses.append(COMPLETE_VERSE[:i])
        i += 1
    # Add thats and compile into string
    verses = [ " that ".join(reversed(verse)) for verse in verses ]
    print(verses)
    # Start with This is
    for idx, verse in enumerate(verses):
        the_index = verse.find("the")
        verses[idx] = "This is " + verse[the_index:]
    
    return verses