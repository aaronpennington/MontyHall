import random

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

def end_message(second_door, prize_door, pick, switch):
    if switch == 'y':
        print("You switched to Door #" + str(second_door) + ".")
        new_pick = second_door
    elif switch == 'n':
        print("You stuck with Door #" + str(pick) + ".")
        new_pick = pick

    print("The prize was behind Door #" + str(prize_door) + ".")
    
    if is_prize_door(prize_door, new_pick):
        print("YOU WIN!")
    else:
        print("YOU LOSE!")

def __main__():
    # The classic problem uses 3 doors. However, you can have as many doors as you want here. But only 2 will be left closed after the first choice. 
    num_doors = 3

    # Random door is assigned the prize
    prize_door = random.randint(0, num_doors-1)
    
    # User picks door
    pick = pick_door(num_doors)

    # All doors will be opened EXCEPT FOR two doors. One of the unopened doors must contain the prize. The other must not.
    
    # Therefore, we want to find out if the player has picked the prize door or not. 
    picked_prize = is_prize_door(prize_door, pick)

    # IF the player picked the prize door, we need a second random door as a decoy. 
    if picked_prize:
        fake_door = get_fake_door(num_doors, pick)

        # Give the player the option to switch doors. 
        switch = switch_door(pick, fake_door)

        # IF the player decides to switch, then we need to flip the state of the picked door. 
        end_message(fake_door, prize_door, pick, switch)
    
    # IF the player did not pick the prize door, then the prize door will be the 'decoy'. 
    elif not picked_prize:
        # Give the player the option to switch doors. 
        switch = switch_door(pick, prize_door)

        # IF the player decides to switch, then we need to flip the state of the picked door. 
        end_message(prize_door, prize_door, pick, switch)

if __name__ == "__main__":
    __main__()  
