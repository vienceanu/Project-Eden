import json


class Trader:
    money = 10000000000
    minerals =  { "Uranium": 50, "Iron": 10, "Titanium": 20, "Water": 1, "Hydrogen":1, "Helium": 3, }
    
def buy_mode(doge, Resources):
    print(f"Welcome to my shop!\n Here are the current listing!\n")
    print(json.dumps(Trader.minerals, indent=4, sort_keys=True))
    
buy_mode(1, 1)