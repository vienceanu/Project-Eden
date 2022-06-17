import json
import random
import navigation
from Ship import *

def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)
        


def buy_mode(doge, Resources):
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
        elif answer == "back":
            navigation.trader_mode()
        else:
            print(f"Incorrect Selection\n")

def sell_mode(doge, Resources):
    with open("data.json", "r") as f:
        data = json.load(f)
    while True:
        print(f"Welcome to my shop!\n What do you wish to sell?\n")
        print(json.dumps(Ship.Resources, indent=4, sort_keys=True))
        answer = input("What are you selling? ").lower()
        if answer in Ship.Resources and Ship.Resources[answer] > 0:
                confirm = input(f"Are you sure you wish to sell {answer}? y/n \n").lower()
                if confirm == "y":
                    Ship.doge += Trader.minerals[answer]
                    data['ship']['Doge'] = Ship.doge
                    print(f"Your new wallet balance is: {Ship.doge}\n")
                    Ship.Resources[answer] -= 1
                    data['ship']['Resources'][answer] = Ship.Resources[answer]
                    write_to_json(data)
                elif confirm == "n":
                    print(f"Your new wallet balance is: {Ship.doge}\n")
        elif answer == "back":
            navigation.trader_mode()
        else:
            print(f"Incorrect Selection\n")
            

     
