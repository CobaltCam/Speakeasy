import random

def roll_dice(num_sides: int):
    return f" rolled 1d{num_sides}: you got a {random.randrange(1, num_sides)}"
    
