"""
This module has a function related to pig latin.
"""

def translate(text: str) -> str:
    """
    Function that translates from english to pig latin.

    text: str - the text to translate (english).
    return: str - the translated output (pig latin).
    """

    #Remove unwanted spaces
    text = text.rstrip()
    text = text.lstrip()

    #Separate words
    words = text.split(" ")
    text = ""

    #Hardcodes
    vowels = ["a","e","i","o","u"]
    
    for word in words:
        #Analize letter by letter
        if word[0] in vowels or word[0:2] in ["xr","yt"]:
            pass #just add "ay"
        else: #starts with a consonant
            while not word[0] in vowels: #while the first letter is a consonant
                word = word.removeprefix(word[0]) + word[0] #move consonant to the end
                if word[0] == "y":
                    break
            if word[0] == "u" and word[len(word)-1] == "q": #word had "qu"
                word = word.removeprefix(word[0]) + word[0] #move "u" to the end
            if (word[0] == "y") and (not word[len(word)-1] in vowels) and (not word[len(word)-2] in vowels): #word had consonant cluster and y
                pass

        word += "ay"
        text += word + " "
    return text.rstrip()