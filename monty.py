import random

class Door:
    def __init__(self, picked, prize):
        self.picked = picked
        self.prize = prize

def pick_door(num_doors):
    # Here's where we get user input. 
    print("There are " + str(num_doors) + " doors. Behind one door is a prize. The other " + str(num_doors - 1) + " doors are empty.")
    print("Pick one door.")
    pick = int(input("> "))
    return pick

def is_prize_door(prize_door, pick):
    if prize_door == pick:
        return True
    return False

def get_fake_door(num_doors, pick):
    fake_door = random.randint(0, num_doors)
    # Keep getting a random door until it is not the same as the picked door. 
    if fake_door == pick:
        get_fake_door(num_doors, pick)
    return fake_door

def switch_door(pick, second_door):
    print("You have chosen Door #" + str(pick) + ".")
    print("All of the other doors have been opened except for Door #" + str(second_door) + ".")
    print("You may choose to switch doors, or stick with your original choice.")
    print("Would you like to switch?")
    switch = input("y/n: ")
    return switch

def __main__():
    all_doors = []
    num_doors = 3

    # Fills the array with doors. 
    while (len(all_doors) < num_doors):
        door = Door(False, False)
        all_doors.append(door)

    # Random door is assigned the prize
    prize_door = random.randint(0, num_doors)
    all_doors[prize_door].prize = True
    
    # User picks door
    pick = pick_door(num_doors)
    all_doors[pick].picked = True

    # All doors will be opened EXCEPT FOR two doors. One of the unopened doors must contain the prize. The other must not.
    
    # Therefore, we want to find out if the player has picked the prize door or not. 
    picked_prize = is_prize_door(prize_door, pick)

    # IF the player picked the prize door, we need a second random door as a decoy. 
    if picked_prize:
        fake_door = get_fake_door(num_doors, pick)

        # Give the player the option to switch doors. 
        switch = switch_door(pick, fake_door)

        # IF the player decides to switch, then we need to flip the state of the picked door. 
        if switch == 'y':
            all_doors[pick].picked = False
            all_doors[fake_door].picked = True
            print("You switched to Door #" + str(fake_door) + ".")
            print("Sorry, the prize was behind Door #" + str(prize_door) + ".")
            print("YOU LOSE!")
            print("Next time, try not switching.")

        elif switch == 'n':
            print("You did not switch doors.")
            print("Congrats! The prize was behind Door #" + str(prize_door) + ".")
            print("YOU WIN!")
    
    # IF the player did not pick the prize door, then the prize door will be the 'decoy'. 
    elif not picked_prize:
        # Give the player the option to switch doors. 
        switch = switch_door(pick, prize_door)

        # IF the player decides to switch, then we need to flip the state of the picked door. 
        if switch == 'y':
            all_doors[pick].picked = False
            all_doors[prize_door].picked = True
            print("You switched to Door #" + str(prize_door) + ".")
            print("Congrats! The prize was behind Door #" + str(prize_door) + ".")
            print("YOU WIN!")

        elif switch == 'n':
            print("You did not switch doors.")
            print("Sorry, the prize was behind Door #" + str(prize_door) + ".")
            print("YOU LOSE!")

if __name__ == "__main__":
    __main__() 