import json
from Ship import Ship
from navigation import *

class Trader:
    money = 10000000000
    minerals =  { "uranium": 50, "iron": 10, "titanium": 20, "water": 1, "hydrogen":1, "helium": 3, }


def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)

def buy_mode(doge, Resources):
    with open("data.json", "r") as f:
        data = json.load(f)
    while True:
        print(f"Welcome to my shop!\n Here are the current listing!\n")
        print(json.dumps(Trader.minerals, indent=4, sort_keys=True))
        val = input("What are you buying? ").lower()
        if val in Trader.minerals:
            if Trader.minerals[val] <= Ship.doge:
                val1 = input(f"Are you sure you wish to purchase {val}? y/n \n").lower()
                if val1 == "y":
                    Ship.doge -= Trader.minerals[val]
                    data['ship']['Doge'] = Ship.doge
                    print(f"Your new wallet balance is: {Ship.doge}\n")
                    Ship.Resources[val] += 1
                    data['ship']['Resources'][val] = Ship.Resources[val]
                    write_to_json(data)
                elif val1 == "n":
                    print(f"Your new wallet balance is: {Ship.doge}\n")
            else:
                print(f"Insufficient funds, why not pick something else?")
        elif val == "exit":
            navigation_mode()
        else:
            print(f"Incorrect Selection\n")

def sell_mode(doge, Resources):
    with open("data.json", "r") as f:
        data = json.load(f)
    while True:
        print(f"Welcome to my shop!\n What do you wish to sell?\n")
        print(json.dumps(Ship.Resources, indent=4, sort_keys=True))
        val = input("What are you selling? ").lower()
        if val in Ship.Resources and Ship.Resources[val] > 0:
                val1 = input(f"Are you sure you wish to sell {val}? y/n \n").lower()
                if val1 == "y":
                    Ship.doge += Trader.minerals[val]
                    data['ship']['Doge'] = Ship.doge
                    print(f"Your new wallet balance is: {Ship.doge}\n")
                    Ship.Resources[val] -= 1
                    data['ship']['Resources'][val] = Ship.Resources[val]
                    write_to_json(data)
                elif val1 == "n":
                    print(f"Your new wallet balance is: {Ship.doge}\n")
        elif val == "exit":
            navigation_mode()
        else:
            print(f"Incorrect Selection\n")
            
def trader_mode():
    print(f"Welcome to my shop! I have many fine wares!\n") 
    val3 = input(f"Are you making a purchase, or looking to sell?\n").lower()
    if val3 == "help":
        trader_help_file = open("combatHelp.txt")
        trader_contents = trader_help_file.read()
        print(trader_contents)
    elif val3 == "buy":
        buy_mode(Ship.doge, Ship.Resources)
    elif val3 == "sell":
        sell_mode(Ship.doge, Ship.Resources)
    else:
        print(f"")
    if val3 == 'leave':
        navigation_mode()

     
trader_mode()