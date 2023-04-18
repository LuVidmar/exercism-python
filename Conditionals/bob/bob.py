"""
This module has only one function for Bob to respond to questions.
"""

def response(interaction: str) -> str:
    """
    Given an interaction, bob will respond.

    interaction: str - interaction for bob to respond to
    return: str - bob's response
    """
    
    interaction = interaction.rstrip()
    response = "Whatever." #default response

    is_empty: bool = interaction.isspace() or len(interaction) == 0
    has_letters: bool = any(c.isalpha() for c in interaction)
    has_numbers: bool= any(c.isnumeric() for c in interaction)
    is_shouting: bool = interaction.upper() == interaction and has_letters
    is_question: bool = "?" in interaction and interaction.index("?") == len(interaction) - 1
    print("is_empty:" + str(is_empty))
    print("has_letters:" + str(has_letters))
    print("is_shouting:" + str(is_shouting))
    print("is_question:" + str(is_question))
    if is_empty:
        response = "Fine. Be that way!"
    elif is_shouting and is_question:
        response = "Calm down, I know what I'm doing!"
    elif is_shouting and not is_question:
        response = "Whoa, chill out!"
    elif not is_shouting and is_question:
        response = "Sure."
    
    return response