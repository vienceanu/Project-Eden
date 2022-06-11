import json
from Ship import Ship
from navigation import *

class Trader:
    money = 10000000000
    minerals =  { "uranium": 50, "iron": 10, "titanium": 20, "water": 1, "hydrogen":1, "helium": 3, }
    
def buy_mode(doge, Resources):
    while True:
        print(f"Welcome to my shop!\n Here are the current listing!\n")
        print(json.dumps(Trader.minerals, indent=4, sort_keys=True))
        val = input("What are you buying? ").lower()
        if val in Trader.minerals:
            if Trader.minerals[val] <= Ship.doge:
                val1 = input(f"Are you sure you wish to purchase {val}? y/n \n").lower()
                if val1 == "y":
                    Ship.doge -= Trader.minerals[val]
                    print(f"Your new wallet balance is: {Ship.doge}\n")
                    Ship.Resources[val] += 1                    
                elif val1 == "n":
                    print(f"Your new wallet balance is: {Ship.doge}\n")
            else:
                print(f"Insufficient funds, why not pick something else?")
        elif val == "exit":
            navigation_mode()
        else:
            print(f"Incorrect Selection\n")

def sell_mode(doge, Resources):
    while True:
        print(f"Welcome to my shop!\n What do you wish to sell?\n")
        print(json.dumps(Ship.Resources, indent=4, sort_keys=True))
        val = input("What are you selling? ").lower()
        if val in Ship.Resources and Ship.Resources[val] > 0:
                val1 = input(f"Are you sure you wish to sell {val}? y/n \n").lower()
                if val1 == "y":
                    Ship.doge += Trader.minerals[val]
                    print(f"Your new wallet balance is: {Ship.doge}\n")
                    Ship.Resources[val] -= 1
                elif val1 == "n":
                    print(f"Your new wallet balance is: {Ship.doge}\n")
        elif val == "exit":
            navigation_mode()
        else:
            print(f"Incorrect Selection\n")
            
                
            
            
        
    
    
buy_mode(Ship.doge, Ship.Resources)