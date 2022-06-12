import json
from Ship import Ship
from trader import Trader

def load_game():
    with open("data.json", "r") as f:
        data = json.load(f)

    Ship.Inventory = data['ship']['Inventory']
    Ship.Hull = int(data['ship']['Hull'])
    Ship.HP = Ship.Hull * int(data['ship']['HP'])
    Ship.Fuel = int(data['ship']['Fuel'])
    Ship.location = data['ship']['location']
    Ship.Passengers = data['ship']['Passengers']
    Ship.doge = int(data['ship']['Doge'])
    Ship.dockStatus = int(data['ship']['DockStatus'])
    Ship.Resources = data['ship']['Resources']
    Trader.money = data['money']
