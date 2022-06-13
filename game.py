from Load import *
from Ship import *
from navigation import *


exit = False
inputs = ()
def intro():
    name = input("What is your name, cadet?\n")
    print(f"Greetings, {name}. Let's throw you in")
    print("barely clinging to life, all of your alarms are going off, no oxygen, no hope")
    print("How do you proceed?\n")
    print("1). Put on your Oxygen and Repair the Ship\n 2). Abandon all hope and give in")
    answer = input("Your Answer: ")
    if answer == "1":
        print("You put on your seat and begin emergency procedural repairs. You life to fight another day. \n")
        print("You hear a beeping noise coming from the cockpit. How do you proceed? \n")
        print("1). Enter the cockpit \n 2). Wander the ship looking for surroundings")
        answer = input("Your Answer: ")
        if answer == "1":
            print("You enter the cockpit and are greeted by the ships A.I \n")
            print(f"Greetings Captain {name}. I am your Ships A.I Cortana. \n")
            shipintro_file = open("shipsaiintro.txt")
            file_contents = shipintro_file.read()
            print(file_contents)
            navigation_mode()
            
        elif answer == "2":
            print("Game Over")
        else:
            print("Command not recognized")

    elif answer == "2":
        print("Game Over")
        quit()
    else:
        print("Command not recognized")
    
    
def run():
    while exit == False:
        intro()
        
def ctnGame():
    while exit == False:
        load_game()
        navigation_mode()
   
