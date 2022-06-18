import math
import sys
import time
import json
import time
import random
import Monster
from combat import combat
import Upgrading
import descends.mars as mars_landing
import descends.mercury as mercury_landing
import descends.moon as moon_landing
import descends.pluto as pluto_landing
import descends.venus as venus_landing
from Ship import Ship as Ship
from Upgrading import Gun as Gun
from Upgrading import Hull as Hull
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

class Earth:
    Resources = ["You Can't do that Here!"]
    Locations = ["Survivor's Enclave"]

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
    while True:
        decision = input(f"Are you making a purchase, or looking to sell?\n").lower()
        if decision == "help":
            trader_help_file = open("traderHelp.txt")
            trader_contents = trader_help_file.read()
            print(trader_contents)
        elif decision == 'leave':
            navigation_mode()
        elif decision == "buy":
            buy_mode(Ship.doge, Ship.Resources)
        elif decision == "sell":
            sell_mode(Ship.doge, Ship.Resources)
        else:
            print(f"")


#String to Class Object
def str_to_class(str):
    return getattr(sys.modules[__name__], str.capitalize())

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
                    Ship.Inventory['LG'] = math.pow(2, Ship.LGLevel) + 6
                    data['ship']['Inventory']['LG'] = Ship.Inventory['LG']
                    data['ship']['LGLevel'] = Ship.LGLevel
                    write_to_json(data)
                    print("Upgrade complete.")
                    print("Your Laser Gun is now level " + str(Ship.LGLevel))

                else:
                    print("You do not have enough resources to upgrade.")
                break
            elif answer == "n":
                print("Upgradation cancelled.")
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
    global cur_location

    with open("data.json", "r") as f:
        data = json.load(f)

    cur_location = Ship.location

    print("You drift Motionless through space\n")
    #############################
    print(Trader.location)
    ################################
    if Ship.location == Trader.location or Ship.location == Trader1.location:
        print(f"There is a trader convoy at your current location, maybe they have some wares......\n")
    while True:

        answer = input("Your Answer: ").strip()
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
                if Ship.location == "earth":
                    print("You can't do that here!!!")
                else:
                    print(f"Mining.....")
                    #time.sleep(3)
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
                destination = input("Travel Destination:").lower()
                if destination in solar_system and fuel_Check(destination) == True:
                    if destination == "sun":
                        combat(Monster.Alien_Queen.enemy_name, Monster.Alien_Queen.enemy_Hp, Monster.Alien_Queen.enemy_dmg)
                    else:
                        Ship.Fuel -= (abs(return_key(cur_location) - return_key(destination)))
                        Ship.location= destination
                        cur_location = destination
                        data['ship']['Fuel'] = Ship.Fuel
                        data['ship']['location'] = Ship.location
                        write_to_json(data)
                        print(f"Your new location: {Ship.location}")
                        print(f"Fuel Left: {Ship.Fuel}")
                        if random.randint(1,5) == 5:
                            combat()
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
                print("LG damage: " + str(Ship.Inventory['LG']))

        else:
            print("Command not recognized")
            
#navigation mode testing, remove to launch game
navigation_mode()