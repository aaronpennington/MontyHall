# Simulation of the Monty Hall Problem
# Based on my playable implementation of said problem. 

from monty import is_prize_door
import random

def sim(win):
    num_doors = 3

    prize_door = random.randint(0, num_doors-1)

    pick = random.randint(0, num_doors-1)

    picked_prize = is_prize_door(prize_door, pick)

    if picked_prize:
        switch = 'y'

        if switch == 'y': #LOSE
            return win

        elif switch == 'n': #WIN
            return win +1
    
    elif not picked_prize:
        switch = 'y'

        if switch == 'y': #WIN
            return win +1

        elif switch == 'n': #LOSE
            return win

y = 100
x = 0
win = 0
while x < y:
    win = sim(win)
    x = x+1
print("WINS: " + str(win))
print("Percent Won by Switching: " + str((win/y) * 100) + "%")
# You will note that the percentage here is always very close to 66% or 2/3. Like magic!