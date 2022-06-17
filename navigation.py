import sys
import time
import json
import time
import random
import landing
from Ship import Ship as Ship
from Stages import *
import trader

class Trader:
    money = 10000000000
    minerals =  { "uranium": 50, "iron": 10, "titanium": 20, "water": 1, "hydrogen":1, "helium": 3, }
    location = ""

class Mercury:
    Resources = ["Uranium"]
    Locations = ["Uranium Field's"]

class Moon:
    Resources = ["Iron", "Titanium"]
    Locations = ["Moon's Core", "Crater Tycho","Pirates", "Mineral Depository 1"]
    
class Uranus:
    Resources = ["Water"]
    Locations = ["Deux Sommets", "Dangerous Hole"]
    
class Jupiter:
    Resources = ["Hydrogen", "Helium"]
    Locations = ["Mt. Jupiter", "Alien Hole", "Storm's Eye"]


class Neptune:
    Resources = ["Hydrogen", "Helium"]
    Locations = ["Blue Dune", "Azure Ridge", "Cerulean Sea"]

class Venus:
    Resources = ["Iron"]
    Locations = ["Makeout Point", "Aphrodite's Channel", "Clamshell Cove"]
    
class Mars:
    Resources = ["Iron", "Titanium"]
    Locations = ["Olympus Mons", "South Pole", "The Great Desert"]
    
class Pluto:
    Resources = ["Iron", "Titanium"]
    Locations = ["Pirate Hideout", "Endles Tundra"]
    
class Sun:
    Resources = ["Ore-X"]
    Locations = ["Orbit"]


#Data 
landable_planet=["mercury", "venus", "earth", "mars", "pluto", "moon"]
fuel = Ship.Fuel
verbs = ["map", "travel", "survey", "mine", "status", "help", "trade", "craft" ]
solar_system = {"sun":0, "mercury":15, "venus":23, "earth":30, "moon":31, "mars": 36, "jupiter":45, 
                "saturn": 53, "uranus": 68, "neptune": 79, "pluto": 120 }

def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)

def trader_mode():
    print(f"Welcome to my shop! I have many fine wares!\n") 
    decision = input(f"Are you making a purchase, or looking to sell?\n").lower()
    if decision == "help":
        trader_help_file = open("traderHelp.txt")
        trader_contents = trader_help_file.read()
        print(trader_contents)
    elif decision == 'leave':
        navigation_mode()
    elif decision == "buy":
        trader.buy_mode(Ship.doge, Ship.Resources)
    elif decision == "sell":
        trader.sell_mode(Ship.doge, Ship.Resources)
    else:
        print(f"")


#String to Class Object
def str_to_class(str):
    return getattr(sys.modules[__name__], str)

#Finds the distance position of a planet
def return_key(destination):
    for key, value in solar_system.items():
        if key==destination:
            return int(value)
        
def trader_planet_move(dictionary, n):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
#checks if we have enough fuel, 
def fuel_Check(destination):
    return fuel >= abs(return_key(cur_location) - return_key(destination))

# #testing trader
# trader2 = trader_planet_move(solar_system)


def navigation_mode():
    global cur_location
    with open("data.json", "r") as f:
        data = json.load(f)
    cur_location = "Pluto"
    print("You drift Motionless through space\n")
    print(Trader.location)
    if Ship.location == Trader.location:
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
            elif answer == "descend" and answer in landable_planet:
                print(f"Descending into {Ship.location} \n")
                landing.descend()
                
            elif answer == "mine":
                print(f"Mining.....")
                time.sleep(3)
                arr = str_to_class(Ship.location).Resources
                for i in range(len(arr)):
                    Ship.Resources[arr[i].lower()] += 2
                    data['ship']['Resources'][arr[i].lower()] = Ship.Resources[arr[i].lower()]
                print(f"sucesffuly mined 2 x {str_to_class(Ship.location).Resources}")
            elif answer == "trade" and Ship.location == Trader.location:
                trader_mode()
            elif answer == "exit" :
                data['ship']['location'] == ""
                quit()
            elif answer == "travel":
                print(f"You are currently at {Ship.location}. Where would you like to travel?")
                val1 = input("Travel Destination:").lower()
                if val1 in solar_system :
                    print(cur_location)
                    #156 doesnt return teh right type
                    # Ship.Fuel -= (abs(return_key(cur_location) - return_key(val1)))
                    Ship.location= val1
                    cur_location = val1
                    data['ship']['Fuel'] = Ship.Fuel
                    data['ship']['location'] = Ship.location
                    write_to_json(data)
                    print(cur_location)

                    print(f"Your new location: {Ship.location}")
                    print(f"Fuel Left: {Ship.Fuel}")
                    print(f"initialized trader location: {Trader.location}")
                    Trader.location == ""
                    print(f"cleared trader location : {Trader.location}")
                    
                    Trader.location == trader_planet_move(solar_system, random.randint(1,9))
                    print(f"new trader location: {Trader.location}")
                    
                    navigation_mode()


                # Add a differentiation between fuel and not being able to travel.
                else:
                    print("Cannot travel")
        else:
            print("Command not recognized")
            
#navigation mode testing, remove to launch game
# navigation_mode()
print(return_key('pluto'))