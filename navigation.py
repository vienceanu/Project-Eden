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
def fuel_Check(destination):
    return fuel >= abs(return_key(location) - return_key(destination))
  



def navigation_mode():
    print("You drift Motionless through space\n")
    while Ship.dockStatus == 0:
        val = input("Your Answer: ")
        if val in verbs:
            if val == "map":
                print("Here is the map\n")
                print()
                print(f"you are currently at {Ship.location}")
            elif val == "survey":
                print("Resources at current planet are:")
                print("Resources")
            elif val == "travel":
                print(f"You are currently at {Ship.location}. Where would you like to travel?")
                val1 = input("Travel Destination:")
                if isinstance(abs(return_key(location) - return_key(val1)), int) and fuel_Check(val1) == True:
                    Ship.Fuel -= (abs(return_key(location) - return_key(val1)))
                    Ship.location = val1
                    print(Ship.location)
                    print(Ship.Fuel)
                # Add a differentiation between fuel and not being able to travel.    
                else:
                    print("Cannot travel")  
        else:
            print("Command not recognized")
    