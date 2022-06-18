import json
import random
from Ship import *

def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)
        
class Trader:
    money = 10000000000
    minerals =  { "uranium": 50, "iron": 10, "titanium": 20, "water": 1, "hydrogen":1, "helium": 3, "torpedo":3 }
    location = "pluto"

class Trader1:
    money = 10000000000
    minerals =  { "uranium": 50, "iron": 10, "titanium": 20, "water": 1, "hydrogen":1, "helium": 3, "torpedo" : 1}
    location = "moon"

def buy_mode():
    with open("data.json", "r") as f:
        data = json.load(f)
    while True:
        print(f"Welcome to my shop!\n Here are the current listing!\n")
        print(json.dumps(Trader.minerals, indent=4, sort_keys=True))
        answer = input("What are you buying? ").lower()
        if answer in Trader.minerals:
            if Trader.minerals[answer] <= Ship.doge:
                confirm = input(f"Are you sure you wish to purchase {answer}? y/n \n").lower()
                if confirm == "y":
                    Ship.doge -= Trader.minerals[answer]
                    data['ship']['Doge'] = Ship.doge
                    print(f"Your new wallet balance is: {Ship.doge}\n")
                    Ship.Resources[answer] += 1
                    data['ship']['Resources'][answer] = Ship.Resources[answer]
                    write_to_json(data)
                elif confirm == "n":
                    print(f"Your new wallet balance is: {Ship.doge}\n")
            else:
                print(f"Insufficient funds, why not pick something else?")
        elif answer == "exit":
            navigation_mode()
        else:
            print(f"Incorrect Selection\n")

def sell_mode():
    with open("data.json", "r") as f:
        data = json.load(f)
    while True:
        print(f"Welcome to my shop!\n What do you wish to sell?\n")
        print(json.dumps(Ship.Resources, indent=4, sort_keys=True))
        item = input("What are you selling? ").lower()
        if item in Ship.Resources and Ship.Resources[item] > 0:
                confirm = input(f"Are you sure you wish to sell {item}? y/n \n").lower()
                if confirm == "y":
                    Ship.doge += Trader.minerals[item]
                    data['ship']['Doge'] = Ship.doge
                    print(f"Your new wallet balance is: {Ship.doge}\n")
                    Ship.Resources[item] -= 1
                    data['ship']['Resources'][item] = Ship.Resources[item]
                    write_to_json(data)
                elif confirm == "n":
                    print(f"Your new wallet balance is: {Ship.doge}\n")
        elif item == "exit":
            navigation_mode()
        else:
            print(f"Incorrect Selection\n")
            

     
