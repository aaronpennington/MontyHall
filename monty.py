import random

class Door:
    def __init__(self, picked, prize):
        self.picked = picked
        self.prize = prize
        self.opened = False

def get_fake_door(num_doors, pick):
    fake_door = random.randint(0, num_doors)
    if fake_door == pick:
        get_fake_door(num_doors, pick)
    return fake_door

def __main__():
    all_doors = []
    num_doors = 3

    while (len(all_doors) < num_doors):
        door = Door(False, False)
        all_doors.append(door)

    prize_door = random.randint(0, num_doors)
    for door in all_doors:
        if door == prize_door:
            door.prize = True
    
    print("There are " + str(num_doors) + " doors. Behind one door is a prize. The other " + str(num_doors - 1) + " doors are empty.")
    pick = int(input("Pick one door. >")) -1
    all_doors[pick].picked = True

    if prize_door == pick:
        fake_door = get_fake_door(num_doors, pick)
    else:
        fake_door = pick

    for door in all_doors:
        if not (door.picked or door.prize):
            if fake_door != door:
                door.opened = True

    if pick == prize_door:
        print("The prize is either behind door #" + str(pick) + " (the one you picked), or behind door #" + str(fake_door))
    elif pick != prize_door:
        print("The prize is either behind door #" + str(pick) + " (the one you picked), or behind door #" + str(prize_door))

    print("Do you want to switch to the other door?")
    switch = input("(y/n) >")
    if switch == "y":
        if pick == prize_door:
            print("Sorry, the prize was behind the original door!")
            print("YOU LOSE!")
        elif pick != prize_door:
            print("Congratulations, the prize was behind door #" + str(prize_door))
            print("YOU WIN!")
    elif switch == "n":
        if pick == prize_door:
            print("Congratulations, the prize was behind door #" + str(prize_door))
            print("YOU WIN!")
        elif pick != prize_door:
            print("Sorry, the prize was behind the original door!")
            print("YOU LOSE!")


if __name__ == "__main__":
    __main__() 
