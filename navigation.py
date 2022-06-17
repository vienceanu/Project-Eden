import sys
import time
import json
import time
import random
import descends.mars as mars_landing
import descends.mercury as mercury_landing
import descends.moon as moon_landing
import descends.pluto as pluto_landing
import descends.venus as venus_landing
from Ship import Ship as Ship
from Stages import *
import trader

class Trader:
    money = 10000000000
    minerals =  { "uranium": 50, "iron": 10, "titanium": 20, "water": 1, "hydrogen":1, "helium": 3, }
    location = "pluto"

class Trader1:
    money = 10000000000
    minerals =  { "uranium": 50, "iron": 10, "titanium": 20, "water": 1, "hydrogen":1, "helium": 3, }
    location = "moon"

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
landable_planet=["mercury", "venus", "mars", "pluto", "moon"]
fuel = Ship.Fuel
verbs = ["map", "travel", "survey", "mine", "status", "help", "trade", "craft","descend" ]



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
    return solar_system.get(destination)

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
def fuel_Check(destination):
    return fuel >= abs(return_key(cur_location) - return_key(destination))


def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)
        


def buy_mode(doge, Resources):
    with open("data.json", "r") as f:
        data = json.load(f)
    while True:
        print(f"Welcome to my shop!\n Here are the current listing!\n")
        print(json.dumps(Trader.minerals, indent=4, sort_keys=True))
        answer = input("What are you buying? ").lower()
        if answer in Trader.minerals:
            if Trader.minerals[answer] <= Ship.doge:
                confirm = input(f"Are you sure you wish to purchase {answer}? y/n \n").lower()
                if confirm == "y":
                    Ship.doge -= Trader.minerals[answer]
                    data['ship']['Doge'] = Ship.doge
                    print(f"Your new wallet balance is: {Ship.doge}\n")
                    Ship.Resources[answer] += 1
                    data['ship']['Resources'][answer] = Ship.Resources[answer]
                    write_to_json(data)
                elif confirm == "n":
                    print(f"Your new wallet balance is: {Ship.doge}\n")
            else:
                print("Insufficient funds, why not pick something else?")
        elif answer == "back":
            trader_mode()
        else:
            print("Incorrect Selection\n")

def sell_mode(doge, Resources):
    with open("data.json", "r") as f:
        data = json.load(f)
    while True:
        print("Welcome to my shop!\n What do you wish to sell?\n")
        print(json.dumps(Ship.Resources, indent=4, sort_keys=True))
        answer = input("What are you selling? ").lower()
        if answer in Ship.Resources and Ship.Resources[answer] > 0:
                confirm = input(f"Are you sure you wish to sell {answer}? y/n \n").lower()
                if confirm == "y":
                    Ship.doge += Trader.minerals[answer]
                    data['ship']['Doge'] = Ship.doge
                    print(f"Your new wallet balance is: {Ship.doge}\n")
                    Ship.Resources[answer] -= 1
                    data['ship']['Resources'][answer] = Ship.Resources[answer]
                    write_to_json(data)
                elif confirm == "n":
                    print(f"Your new wallet balance is: {Ship.doge}\n")
        elif answer == "back":
            trader_mode()
        else:
            print("Incorrect Selection\n")
            
def navigation_mode():
    global cur_location
    with open("data.json", "r") as f:
        data = json.load(f)
    cur_location = "pluto"
    print("You drift Motionless through space\n")
    #############################
    print(Trader.location)
    ################################
    if Ship.location == Trader.location or Trader1.location:
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
                time.sleep(3)
                arr = str_to_class(Ship.location).Resources
                for i in range(len(arr)):
                    Ship.Resources[arr[i].lower()] += 2
                    data['ship']['Resources'][arr[i].lower()] = Ship.Resources[arr[i].lower()]
                print(f"sucesffuly mined 2 x {str_to_class(Ship.location).Resources}")
            elif answer == "trade" and Ship.location == Trader.location:
                trader_mode()
            elif answer == "trade" and Ship.location == Trader1.location:
                trader_mode()
            elif answer == "exit" :
                data['ship']['location'] == ""
                quit()
            elif answer == "travel":
                print(f"You are currently at {Ship.location}. Where would you like to travel?")
                val1 = input("Travel Destination:").lower()
                if val1 in solar_system and fuel_Check(val1) == True:
                    print(cur_location)
                    Ship.Fuel -= (abs(return_key(cur_location) - return_key(val1)))
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
                    Trader.location == trader_planet_move(solar_system)
                    print(f"new trader location: {Trader.location}")
                    
                    navigation_mode()


                # Add a differentiation between fuel and not being able to travel.
                else:
                    print("Cannot travel")
        else:
            print("Command not recognized")
            
#navigation mode testing, remove to launch game
navigation_mode()