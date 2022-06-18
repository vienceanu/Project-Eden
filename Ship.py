import math
class Ship:
    #weapons
    LGLevel = 1
    Inventory ={"LG": math.pow(2,LGLevel) + 6, "Tor": 10}
    HullLevel = 1
    Hull = 1.2
    HP = 50 * Hull
    #Testing for trader
    Fuel = 100000
    location = "pluto"
    Passengers = []
    doge = 10000
    #Dock status, if docked 1 else 0
    dockStatus = 0
    quest_item = []
    #For resources need a dictionary
    Resources = {"uranium": 0, "iron": 0, "titanium": 0, "water": 0, "hydrogen": 0, "helium": 0, "ore-x": 0, "torpedo": 0}
    
    
