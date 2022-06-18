import sys
import time
import json
import time
import random

from combat import *
from Ship import Ship as Ship
from Stages import *
from trader import *
 
landable_planet=["mercury", "venus", "mars", "pluto", "moon"]
fuel = Ship.Fuel
verbs = ["map", "travel", "survey", "mine", "status", "help", "trade", "craft","descend" ]

def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)

#String to Class Object
def str_to_class(str):
    return getattr(sys.modules[__name__], str.capitalize())

#Finds the distance position of a planet
def distance(planet):
    return solar_system.get(planet)

solar_system = {"sun":0, "mercury":15, "venus":23, "earth":30, "moon":31, "mars": 36, "jupiter":45, 
                "saturn": 53, "uranus": 68, "neptune": 79, "pluto": 120 }
        
def trader_planet_move(dictionary):
    # if n < 0:
    #     n += len(dictionary)
    # for i, key in enumerate(dictionary.keys()):
    #     if i == n:
    #         return key
    random.choice(list(dictionary.keys()))
       
#checks if we have enough fuel, 
def fuel_Check(planet):
    return fuel >= abs(distance(cur_location) - distance(planet))

def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)


def upgrading_mode():

    while True:
        with open("data.json", "r") as f:
            data = json.load(f)
        print("Your Laser Gun is at level " + str(Ship.LGLevel))
        print("Your Ship Hull is at level " + str(Ship.HullLevel))
        upgrade = input("What would you like to upgrade?: ").lower()
        if upgrade == "lg":
            if Ship.LGLevel == 5:
                print("You are at the max level for Laser Gun.")
                break
            print("You need the below resources to upgrade Laser Gun to the next level:")
            for item in list(Upgrading.Gun.Resources.keys()):
                print(str(item) + ": " + str((Upgrading.Gun.Resources[item] * Ship.LGLevel)))
            answer = input(print("Do you want to upgrade? Enter y or n:")).lower()
            if answer == "y":
                enough = True
                for item in Upgrading.Gun.Resources:
                    if Ship.Resources[item] < Upgrading.Gun.Resources[item]:
                        enough = False
                        break
                if enough:
                    for item in Upgrading.Gun.Resources:
                        Ship.Resources[item] -= Upgrading.Gun.Resources[item]
                        data['ship']['Resources'][item] = Ship.Resources[item]
                        write_to_json(data)
                    Ship.LGLevel = Ship.LGLevel + 1
                    data['ship']['LGLevel'] = Ship.LGLevel
                    write_to_json(data)
                    print("Upgrade complete.")
                    print("Your Laser Gun is now level " + str(Ship.LGLevel))
                else:
                    print("You do not have enough resources to upgrade.")
                break
            elif answer == "n":
                print("Upgrading cancelled.")
            else:
                print("Command not recognized")
        elif upgrade == "hull":
            if Ship.HullLevel == 5:
                print("You are at the max level for Ship Hull.")
                break
            print("You need the below resources to upgrade Ship Hull to the next level:")
            for item in list(Upgrading.Hull.Resources.keys()):
                print(str(item) + ": " + str((Upgrading.Hull.Resources[item] * Ship.HullLevel)))

            answer = input(print("Do you want to upgrade? Enter y or n:")).lower()
            if answer == "y":
                enough = True
                for item in Upgrading.Hull.Resources:
                    if Ship.Resources[item] < Upgrading.Hull.Resources[item]:
                        enough = False
                        break
                if enough:
                    for item in Upgrading.Hull.Resources:
                        Ship.Resources[item] -= Upgrading.Hull.Resources[item]
                        data['ship']['Resources'][item] = Ship.Resources[item]
                    Ship.HullLevel += 1
                    data['ship']['HullLevel'] = Ship.HullLevel
                    write_to_json(data)
                    print("Upgrade complete.")
                    print("Your Ship Hull is now level " + str(Ship.HullLevel))
                else:
                    print("You do not have enough resources to upgrade.")
                break
            elif answer == "n":
                print("Upgradation cancelled.")
            else:
                print("Command not recognized")
        elif upgrade == "leave":
            break
        else:
            print("Command not recognized")

def navigation_mode():
    # with open("data.json", "r") as f:
    #     data = json.load(f)
    Ship.location
    print("You drift Motionless through space\n")

    if Ship.location == Trader.location or Ship.location == Trader1.location:
        print(f"There is a trader convoy at your current location, maybe they have some wares......\n")
    while Ship.dockStatus == 0:

        answer = input("Your Answer: ")
        if answer in verbs:
            if answer == "map":
                print("Here is the map\n")
                print(solar_system)
                print(f"you are currently at {Ship.location}")
            elif answer =='help':
                navigation_help_file = open("navigationHelp.txt")
                file_contents1 = navigation_help_file.read()
                print(file_contents1)
            elif answer == "status":
                print(f"Resources on the Ship are: {Ship.Resources} \n")
                print(f"Fuel on the Ship is: {Ship.Fuel}\n")
                print(f"Location of the Ship is: {Ship.location}\n")
            elif answer == "survey":
                print(f"Resources at {Ship.location} are:\n")
                print(str_to_class(Ship.location).Resources)
            elif answer == "descend" and Ship.location in landable_planet:
                if Ship.location == "mars":
                    print(f"Descending into {Ship.location} \n")
                    mars_landing.descend()
                elif Ship.location == "mercury":
                    print(f"Descending into {Ship.location} \n")
                    mercury_landing.descend()
                elif Ship.location == "moon":
                    print(f"Descending into {Ship.location} \n")
                    moon_landing.descend()
                elif Ship.location == "pluto":
                    print(f"Descending into {Ship.location} \n")
                    pluto_landing.descend()
                elif Ship.location == "venus":
                    print(f"Descending into {Ship.location} \n")
                    venus_landing.descend()
                ###insert the string form the list to access the file.

            elif answer == "mine":
                print(f"Mining.....")
                #time.sleep(3)
                arr = str_to_class(Ship.location).Resources
                for i in range(len(arr)):
                    Ship.Resources[arr[i].lower()] += 2
                    data['ship']['Resources'][arr[i].lower()] = Ship.Resources[arr[i].lower()]
                print(f"succesffuly mined 2 x {str_to_class(Ship.location).Resources}")
            elif answer == "trade" and Ship.location == Trader.location:
                trader_mode()
            elif answer == "trade" and Ship.location == Trader1.location:
                trader_mode()
            elif answer == "exit" :
                data['ship']['location'] == ""
                quit()
            elif answer == "travel":
                print(f"You are currently at {Ship.location}. Where would you like to travel?")
                destination = input("Travel Destination:").lower()
                if destination in solar_system and fuel_Check(destination) == True:
                    print(cur_location)
                    Ship.Fuel -= (abs(distance(cur_location) - distance(destination)))
                    Ship.location= destination
                    cur_location = destination
                    data['ship']['Fuel'] = Ship.Fuel
                    data['ship']['location'] = Ship.location
                    write_to_json(data)
                    print(cur_location)
                    print(f"Your new location: {Ship.location}")
                    print(f"Fuel Left: {Ship.Fuel}")
                    print(f"initialized trader location: {Trader.location}")
                    Trader.location == ""
                    print(f"cleared trader location : {Trader.location}")
                    Trader.location == trader_planet_move(solar_system)
                    print(f"new trader location: {Trader.location}")
                    
                    navigation_mode()


                # Add a differentiation between fuel and not being able to travel.
                else:
                    print("Cannot travel")
            elif answer == "craft":
                print("Welcome to the crafting workshop!")
                print("You can upgrade things here")
                print("Enter LG to upgrade laser gun")
                print("Enter hull to upgrade Ship Hull")
                print("Enter leave to leave the crafting workshop")
                upgrading_mode()

        else:
            print("Command not recognized")
            
#navigation mode testing, remove to launch game
#navigation_mode()
a = 5
b = 2 + 2
c = 5

if c == b or c==a:
    print("suc")