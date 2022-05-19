from Ship import Ship as Ship

#Data 
location = Ship.location
verbs = ["map", "travel", "survey", "mine",  ]
solar_system = {"Sun":0, "Mercury":15, "Venus":23, "Earth":30, "Mars": 36, "Jupiter":45, 
                "Saturn": 53, "Uranus": 68, "Neptune": 79, "Pluto": 120 }

def navigation_mode():
    while Ship.dockStatus == 0:
        print("You drift Motionless through space\n")
        val = input("Your Answer: ")
    if val in verbs:
        if val == "map":
            print("Here is the map\n")
            print()
            print(f"you are currently at {location}")

    elif val == "2":
        print("Game Over")
        quit()
    else:
        print("Command not recognized")
    