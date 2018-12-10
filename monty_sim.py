# Simulation of the Monty Hall Problem
# Based on my playable implementation of said problem. 
# This simulation is hardcoded to always switch doors, 
# in order to show that this is the most efficient strategy
# to win the game. 

from monty import is_prize_door
import random

def sim(win):
    num_doors = 3

    prize_door = random.randint(0, num_doors-1)
    pick = random.randint(0, num_doors-1)
    picked_prize = is_prize_door(prize_door, pick)

    if picked_prize: # This will inevitably be a loss, because the computer originally chose the prize door, but is hardcoded to switch. :o
        return win
    
    elif not picked_prize: # This will be a win, because the computer originally chose the wrong door, but will switch to the correct one, since that's the only door left to switch to. 
        return win+1

y = int(input("How many times do you want to run the simulation?> "))
x = 0
win = 0
while x < y:
    win = sim(win)
    x = x+1
print("WINS: " + str(win))
print("Percent Won by Switching: " + str((win/y) * 100) + "%")
# You will note that the percentage here is always very close to 66% or 2/3. Like magic!