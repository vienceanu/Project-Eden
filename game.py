from Stages import *
from Monster import *
from Ship import Ship as Ship


#this will be used to store the stage name and required item if any to go
stages = {"Mercury": "Item1", "Moon": "Item1", 
          "Uranus": "Item1", "Jupiter": "Item1", 
          "Venus": "Item1", "Mars": "Item1"
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
    val = input("Your Answer: ")
    
    
    
def run():
    while exit == False:
        start()