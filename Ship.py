from xml.dom.domreg import well_known_implementations


class Ship:
    Weapons ={"LG": 2, "Tor": 10}
    Hull = 1.2
    MaxHP = 50 * Hull
    HP = MaxHP
    #Testing for trader
    Fuel = 40
    location = "Pluto"
    Passengers = []
    Money = 10000
    #Dock status, if docked 1 else 0
    dockStatus = 0
    Resources = {"uranium": 1, "iron": 0, "titanium": 0, "water": 0, "hydrogen": 0, "helium": 0, "ore-X": 0, "torpedo": 1}
    
    
