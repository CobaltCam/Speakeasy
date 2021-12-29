import random

rolls = []

def roll_dice(num_dice: int, num_sides: int):
    roll = 0
    global rolls
    rolls.clear()
    for i in range(0, num_dice):
        roll += random.randrange(1, num_sides)
        rolls.append(roll)

    return roll
