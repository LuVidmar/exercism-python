"""
This modules has the data and functions to play a darts game
"""

OUTER_RADIUS = 10
MIDDLE_RADIUS = 5
INNER_RADIUS = 1

def score(x: int, y: int) -> int:
    """
    Recieves coordinates of darts, returns the score

    x, y: int - coordinates of dart
    return: int - score points
    """

    distance_to_center = (x ** 2 + y ** 2) ** (1/2)
    
    print(distance_to_center)

    if MIDDLE_RADIUS < distance_to_center <= OUTER_RADIUS:
        return 1 # inside outer ring
    elif INNER_RADIUS < distance_to_center <= MIDDLE_RADIUS:
        return 5 # inside middle ring
    elif distance_to_center <= INNER_RADIUS:
        return 10 # inside inner ring
    else:
        return 0 # outside board