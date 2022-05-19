from unused.Stages import *
from Monster import *
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
def start():
    name = input("What is your name, cadet?\n")
    print(f"Greetings, {name}. Let's throw you in")
    print("barely clinging to life, all of your alarms are going off, no oxygen, no hope")
    print("How do you proceed?\n")
    print("1). Put on your Oxygen and Repair the Ship\n 2). Abandon all hope and give in")
    val = input("Your Answer: ")
    if val == 1:
        print("You put on your seat and begin emergency procedural repairs. You life to figh tanother day.")
    elif val == 2:
        print("Game Over")
        quit()
    else:
        print("Command not recognized")
    
    
def run():
    while exit == False:
        start()