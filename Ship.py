class Ship:
    def __init__(self):
        self.Inventory ={"LG": 2}
        self.Hull = 1.2
        self.maxHP = 50 * self.Hull
        self.HP = self.maxHP
        self.Fuel = 100
        self.location = "Pluto"
        self.Passengers = []
        #Dock status, if docked 1 else 0
        self.dockStatus = 0
        #For resources need a dictionary
        self.Resources = {"Lithium": 0, "Titanium": 0, "Iron": 0, "Uranium": 0, "Ore-X": 0, "Torpedo": 0}
    
    def getHp(self):
        return self.HP
