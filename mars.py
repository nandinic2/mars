
ch = input("Do you want your spacecraft to be made of gold, iron or steel?")


def level_1a(choice):
    if choice == "gold":
        level_2a = input("Do you want your gold spacecraft to be large, medium or small?")
        if level_2a == "large":
            print("It's too expensive to make.")
        elif level_2a == "medium":
            print("That works.")
            level_3b = input("Do you want to be alone, have 3 people in your team or 5 people")
            if level_3b == "alone":
                print("You went crazy.")
            else:
                print("Too many people, you ran out of resources.")
                level_3c = input("You spent a lot of money on the ship so you can buy only one of the following. Do you want a water purifier, a vegetable garden or a vacuum cleaner?")\
                if level_3c == "water purifier":
                    print("Good choice, you need water to survive!")
                else:
                    print("You died of thirst")

def level_1b(choice):
    if choice == "iron":
        level_2a == input("")
