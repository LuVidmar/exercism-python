"""
This module has a function to solve math problems
"""

def answer(question: str) -> int:
    """
    Given a question, will try to solve the math associated problem.
    Should be formatted: What is 3 plus 2 multiplied by 3?

    question: str - question to solve
    return: int - the result of the math operation
    """
    
    print("1: INPUT: ",question)
    
    # Question starts with What is?
    if question.startswith("What is"):
        question = question.lstrip("What is")
    else:
        raise ValueError("unknown operation")
    
    # Question ends on question mark
    if question.endswith("?"):
        question = question.rstrip("?")
    else:
        raise ValueError("syntax error")
    
    # Replace operators
    question = question.replace("plus", "+")
    question = question.replace("minus", "-")
    question = question.replace("divided by", "/")
    question = question.replace("multiplied by", "*")

    print("2: ",question)

    # Check its a math operation
    valid_chars = "0123456789 +-*/"
    for c in question:
        if valid_chars.find(c) == -1:
            raise ValueError("unknown operation")
        
    print("3: ","Passed validations")

    # Converted to list
    as_list = question.split()
    print("4: ",as_list)

    if len(as_list) == 0:
        raise ValueError("syntax error")

    operators = "/*-+"

    as_list = [ int(l) if l not in operators else l for l in as_list ]

    print("5: ",as_list)

    # Last validation
    # Format: number - operator - number (number odd, operators even)
    for l in as_list[::2]: # odd
        if type(l) is not int:
            raise ValueError("syntax error")
    for l in as_list[1::2]: # even
        if str(l) not in operators:
            raise ValueError("syntax error")
    if type(as_list[-1]) is not int: # last digit must be number
        raise ValueError("syntax error")
        
    print("6: ","All validations passed")

    # Actual operator
    total = as_list.pop(0)
    for o, d in zip(as_list[0::2], as_list[1::2]):
        print(d,o)
        if o == "+":
            total += d
        elif o == "-":
            total -= d
        elif o == "/":
            total /= d
        elif o == "*":
            total *= d
        print(f"total: {total}")
    
    return total