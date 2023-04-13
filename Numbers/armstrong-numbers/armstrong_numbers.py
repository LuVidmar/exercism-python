"""
This module only has a function to determine if a given number is an armstrong number
"""
def is_armstrong_number(number: any) -> bool:
    """
    Takes any number and determines wether its an armstrong number

    :argument number: any - number to analize
    :return: bool
    """

    number_as_string = str(int(number)) #cast it to integer to remove unwanted stuff, then to string to utilize it

    armstrong = 0
    #operate char by char
    for number_as_char in number_as_string: 
        armstrong += int(number_as_char)**len(number_as_string) #sum of each char to the power of the length of string (quantity of digits)

    if (armstrong == number):
        return True
    else:
        return False