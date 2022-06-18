from Load import *
from Ship import *
from navigation import *


exit = False
inputs = ()
def intro():
    print("You wake up, barely clinging to life. Alarms on ship alert you to low oxygen and serious ship damage")
    print("How do you proceed?\n")
    print("1). Put on your Oxygen and Repair the Ship\n 2). Abandon all hope and give in")
    answer = input("Your Answer: ")
    if answer == "1":
        print("Oxygenated air fills your lungs. You spend a few hours repairing the ship back until its only a bit broken")
        print("Sitting down to take a break, you hear a beeping noise coming from the cockpit. How do you proceed? \n")
        print("1). Enter the cockpit \n 2). Wander out the airlock")
        answer = input("Your Answer: ")
        if answer == "1":
            print("You enter the cockpit and are greeted by the ships A.I \n")
            print(f"Greetings cadet. I am your Ships A.I. \n")
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
   
