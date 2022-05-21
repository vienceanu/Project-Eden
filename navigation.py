from Ship import Ship as Ship

#Data 
location = Ship.location
fuel = Ship.Fuel
verbs = ["map", "travel", "survey", "mine",  ]
solar_system = {"Sun":0, "Mercury":15, "Venus":23, "Earth":30, "Mars": 36, "Jupiter":45, 
                "Saturn": 53, "Uranus": 68, "Neptune": 79, "Pluto": 120 }


#Finds the distance position of a planet
def return_key(destination):
    for key, value in solar_system.items():
        if key==destination:
            return int(value)
    return('Key Not Found')

#checks if we have enough fuel, 
def fuel_Check(location, destination):
    return fuel >= abs(return_key(location) - return_key(destination))
  
val1 = str(input("Travel Destination:"))
print(abs(return_key(location) - return_key(val1)))


def navigation_mode():
    while Ship.dockStatus == 0:
        print("You drift Motionless through space\n")
        val = input("Your Answer: ")
    if val in verbs:
        if val == "map":
            print("Here is the map\n")
            print()
            print(f"you are currently at {location}")
    elif val == "survey":
        print("Resources at current planet are:")
        print("Resources")
    elif val == "travel":
        print(f"You are currently at {location}. Where would you like to travel?")
        val1 = input("Travel Destination:")
        if isinstance(abs(return_key(location) - return_key(val1)), int) and fuel_Check(location, val1) == True:
            Ship.Fuel -= (abs(return_key(location) - return_key(val1)))
            Ship.location = "destination"
        else:
            print("Not enough fuel")  
    else:
        print("Command not recognized")
    