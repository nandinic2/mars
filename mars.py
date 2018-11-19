
ch = input("do you want your spacecraft to be made of gold, iron or steel?")

def part_a(choice):
    if choice == "gold":
        #if the player chooses gold
        print("cool choice!")
        level_2 = input("do you want your gold spacecraft to be large, medium or small?")
        if level_2 == "large":
            #if the player chooses large
            print("sorry, it's too expensive to make.")
            quit()
            #Game ends
        elif level_2 == "medium":
            print("that works.")
            level_3 = input("do you want to be alone, have 3 people in your team or 5 people?")
            if level_3 == "alone":
                print("you went crazy.")
                quit()
                #Game ends
            else:
                print("too many people, you ran out of resources.")
                quit()
        elif level_2 == "small":
            print("that works.")
            level_3 = input("you spent a lot of money on the ship so you can buy only one of the following. Do you want a water purifier, a vegetable garden or a vacuum cleaner?")
            sleep(level_3)
            if level_3 == "water purifier":
                print("good choice, you need water to survive!")
                level_4 = input("now that you have taken off, how long do you need to sleep per day in the spacecraft? 3 hours, 6 hours,  13 hours?")
                sleep(level_4)
                #Calls sleep function
                #Game ends
    elif choice == "iron":
        print("cool choice!")
        level_2 = input("do you want candy, diesel or hydrogen fuel to run your spacecraft?")
        if level_2 == "candy":
            print("your spacecraft works.")
            level_3 = input("now that you have taken off, how long do you need to sleep per day in the spacecraft? 3 hours, 6 hours,  13 hours ")
            sleep(level_3)
            #Calls sleep function
        elif level_2 == "diesel":
            print("you die.")
            quit()
            #Game ends
        elif level_2 == "hydrogen fuel":
            print("that works!")
            level_4 == input("now you are in space. You have to choose a direction. Left, straight, right")
            if level_4 == "left":
                print("congratulations! You are now on mars!")
            elif level_4 == "straight":
                print("you’re spaceship got attacked by aliens and you are dead.")
                quit()
                #Game ends
            elif level_4 == "right":
                print("you got sucked into a black hole and you are dead.")
                quit()
                #Game ends
    elif choice == 'steel':
        #if the player chooses steel
        print("good choice!")
        level_2 = input("who would you bring on the spaceship? Scientist, Superman, No one?")
        if level_2 =='scientist':
            #if the player chooses scientist
            print("good choice now you are in space")
            level_3 = input("What do you do to get to mars? Follow the GPS, listen to the scientist, kick out the scientist")
            if level_3 == "follow the GPS":
                #if the player chooses to follow the GPS
                print("you are on Mars. You win!")
            elif level_3 == "listen to the scientist":
                #if the player chooses to listen to the scientist
                print("the scientist is wrong. You are dead.")
                quit()
                #Game ends
            elif level_3 == "kick out the scientist":
                #if the player chooses to kick out the scientist
                print("you are stupid. You are dead")
                quit()
                #Game ends
        elif level_2 == 'superman':
            #if the player chooses superman
            print("superman broke the spaceship, mission failed")
            quit()
            #Game ends
        elif level_2 == 'No one':
            #if the player chooses no one
            print("you bored yourself to death")
            quit()
            #Game ends

def sleep(level):
    if level == "3 hours":
        print("too short, you die.")
        quit()
        #Game ends
    elif level == "6 hours":
        print("too short, you die")
        quit()
        #Game ends
    elif level == "13 hours":
        print("perfect amount of sleep, but you got killed by aliens")
        quit()
        #Game ends

part_a(ch)
