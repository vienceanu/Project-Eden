from Ship import Ship as Ship

#Data 
verbs = ["map", "travel", "survey", "mine",  ]
solar_system = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto" ]

def navigation_mode():
    while Ship.dockStatus == 0:
        print("You drift Motionless through space")
    