from Ship import Ship as Ship
import sys
import json

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

fuel = Ship.Fuel
verbs = ["map", "travel", "survey", "mine", "status" ]
solar_system = {"Sun":0, "Mercury":15, "Venus":23, "Earth":30, "Mars": 36, "Jupiter":45, 
                "Saturn": 53, "Uranus": 68, "Neptune": 79, "Pluto": 120 }

def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)

#String to Class Object
def str_to_class(str):
    return getattr(sys.modules[__name__], str)

#Finds the distance position of a planet
def return_key(destination):
    for key, value in solar_system.items():
        if key==destination:
            return int(value)
    return('Key Not Found')

#checks if we have enough fuel, 
def fuel_Check(destination):
    return fuel >= abs(return_key(cur_location) - return_key(destination))

def navigation_mode():
    global cur_location
    with open("data.json", "r") as f:
        data = json.load(f)
    cur_location = "Pluto"
    print("You drift Motionless through space\n")
    while Ship.dockStatus == 0:
        val = input("Your Answer: ")
        if val in verbs:
            if val == "map":
                print("Here is the map\n")
                print(solar_system)
                print(f"you are currently at {Ship.location}")
            elif val == "status":
                print(f"Resources on the Ship are: {Ship.Resources} \n")
                print(f"Fuel on the Ship is: {Ship.Fuel}\n")
                print(f"Location of the Ship is: {Ship.location}\n")
            elif val == "survey":
                print(f"Resources at {Ship.location} are:")
                print(str_to_class(Ship.location).Resources)
            elif val == "travel":
                print(f"You are currently at {Ship.location}. Where would you like to travel?")
                val1 = input("Travel Destination:")
                if isinstance(abs(return_key(cur_location) - return_key(val1)), int) and fuel_Check(val1) == True:
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
                # Add a differentiation between fuel and not being able to travel.    
                else:
                    print("Cannot travel")  
        else:
            print("Command not recognized")
    
