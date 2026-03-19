# dice_roller.py
import random

def roll_dice(sides=6, rolls=1):
    return [random.randint(1, sides) for _ in range(rolls)]

if __name__ == "__main__":
    sides = int(input("Number of sides: "))
    rolls = int(input("Number of rolls: "))
    results = roll_dice(sides, rolls)
    print("Results:", results)
