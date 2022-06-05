from Stages import *
from Combat.Monster import *
from Ship import Ship as Ship


#this will be used to store the stage name and required item if any to go
stages = {"Mercury": "Item1", "Moon": "Item1", 
          "Uranus": "Item1", "Jupiter": "Item1", 
          "Venus": "Item1", "Mars": "Item1", "Neptune": "Aquatic Upgrade"
          , "Pluto": "Item1", "Sun": "Solar Shielding"}



#These are our monsters
monsters = ("Pirate", "Captain", "Alien", "Alien Queen")

exit = False
inputs = ()
def intro():
    name = input("What is your name, cadet?\n")
    print(f"Greetings, {name}. Let's throw you in")
    print("barely clinging to life, all of your alarms are going off, no oxygen, no hope")
    print("How do you proceed?\n")
    print("1). Put on your Oxygen and Repair the Ship\n 2). Abandon all hope and give in")
    val = input("Your Answer: ")
    if val == "1":
        print("You put on your seat and begin emergency procedural repairs. You life to fight another day. \n")
        print("You hear a beeping noise coming from the cockpit. How do you proceed? \n")
        print("1). Enter the cockpit \n 2). Wander the ship looking for surroundings")
        val = input("Your Answer: ")
        if val == "1":
            print("You enter the cockpit and are greeted by the ships A.I \n")
            print(f"Greetings Captain {name}. I am your Ships A.I Cortana. \n")
            shipintro_file = open("shipsaiintro.txt")
            file_contents = shipintro_file.read()
            print(file_contents)
            
            
        elif val == "2":
            print("Game Over")
        else:
            print("Command not recognized")

    elif val == "2":
        print("Game Over")
        quit()
    else:
        print("Command not recognized")
    
    
def run():
    while exit == False:
        intro()