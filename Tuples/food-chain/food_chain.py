"""
Module that contains functions to generate the lyrics of the song 'I Know an Old Lady Who Swallowed a Fly'
"""

ANIMALS = ["fly", "spider", "bird", "cat", "dog", "goat", "cow" ,"horse"]
VERSE_PATTERN = "She swallowed the {animal1} to catch the {animal2}."
FIRST_SENTENCE = "I know an old lady who swallowed a {animal1}."
SECOND_SENTENCES = [
    "",
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!",
    "She's dead, of course!"
]
END = "I don't know why she swallowed the fly. Perhaps she'll die."

def recite(start_verse: int, end_verse: int) -> list[str]:
    """
    Given a starting and ending verse, will recite the song

    start_verse: int - starting verse
    end_verse: int - ending verse
    return: list[str] - recited song
    """

    # Redefine indexes to fit variables
    start_verse -= 1

    total_verse = []
    # Get all verses
    for i in range(end_verse):
        if i >= start_verse:
            total_verse.append(_recite(i))

    # Format correctly
    formatted = []
    for verse in total_verse:
        formatted.extend(verse)
        formatted.append("")

    # Delete last space
    formatted.pop()

    return formatted

def _recite(until: int) -> list[str]:

    verse: list[str] = []
    # Add first sentence
    verse.append(FIRST_SENTENCE.format(animal1=ANIMALS[until]))
    # Add second sentence
    verse.append(SECOND_SENTENCES[until])

    # Last one is shorter
    if until + 1 >= len(ANIMALS):
        return verse
    
    # Add all animals
    for i in range(until,0,-1):
        if i > 0:
            verse.append(VERSE_PATTERN.format(animal1=ANIMALS[i], animal2=ANIMALS[i-1]))
    # Add last sentence
    verse.append(END)

    # Delete empty line in fly
    if until == ANIMALS.index("fly"):
        verse.pop(-2)

    # Add spider thingies
    if until > ANIMALS.index("spider"):
        verse[-3] = verse[-3].replace("."," that wriggled and jiggled and tickled inside her.")

    print(verse)
    return verse


recite(1, 8),
"""
    "I know an old lady who swallowed a fly.",
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "",
    "I know an old lady who swallowed a spider.",
    "It wriggled and jiggled and tickled inside her.",
    "She swallowed the spider to catch the fly.",
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "",
    "I know an old lady who swallowed a bird.",
    "How absurd to swallow a bird!",
    "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
    "She swallowed the spider to catch the fly.",
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "",
    "I know an old lady who swallowed a cat.",
    "Imagine that, to swallow a cat!",
    "She swallowed the cat to catch the bird.",
    "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
    "She swallowed the spider to catch the fly.",
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "",
    "I know an old lady who swallowed a dog.",
    "What a hog, to swallow a dog!",
    "She swallowed the dog to catch the cat.",
    "She swallowed the cat to catch the bird.",
    "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
    "She swallowed the spider to catch the fly.",
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "",
    "I know an old lady who swallowed a goat.",
    "Just opened her throat and swallowed a goat!",
    "She swallowed the goat to catch the dog.",
    "She swallowed the dog to catch the cat.",
    "She swallowed the cat to catch the bird.",
    "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
    "She swallowed the spider to catch the fly.",
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "",
    "I know an old lady who swallowed a cow.",
    "I don't know how she swallowed a cow!",
    "She swallowed the cow to catch the goat.",
    "She swallowed the goat to catch the dog.",
    "She swallowed the dog to catch the cat.",
    "She swallowed the cat to catch the bird.",
    "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
    "She swallowed the spider to catch the fly.",
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "",
    "I know an old lady who swallowed a horse.",
    "She's dead, of course!",
"""