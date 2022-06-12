from Ship import Ship
import Monster
import time 
import random
import json


global Player_Hp 
Player_Hp = 50

global Player_DMG 
Player_DMGLG = Ship.Inventory["LG"]
Player_DMGTor = Ship.Inventory["Tor"]
Player_DMG = Player_DMGLG

global ename 
ename = "Pirate"

global enemy_dmg 
enemy_dmg= 2

global dmgtoe 
dmgtoe= 0

def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)

# def return_key(destination):
#     for key, value in solar_system.items():
#         if key==destination:
#             return int(value)
#     return('Key Not Found')

def combat_intro():
    print("You encounter an enemy")
    val1 = input("do you wish to try and flee?")
    if val1 == "Flee":
        time.sleep(3)
        print("Sucesfully Fled")
    else:
        print("Get ready for combat!\n")

def combat ():
    global enemy_Hp 
    enemy_Hp = 20
    print(f" {ename} has approached the ship. it readies its weapons\n")
    print("How do you proceeed? \n")
    while enemy_Hp > 0:
        val2 = input("Shoot | Flee | Change Weapon\n").lower()
        if val2 =="shoot":
            dmgtoe = Player_DMG + random.randint(0, 9)
            print(f"Enemy takes {dmgtoe} damage. \n")
            enemy_Hp = enemy_Hp - dmgtoe
            print(f"enemy health = {enemy_Hp}\n")
            print(f"Player takes: {enemy_dmg} and has {Player_Hp} HP left\n")
        elif val2 == "flee":
            player_Flee = random.randint(1,100)
            enemy_Flee = random.randint(1,100)
            if player_Flee > enemy_Flee:
                print(f"You have Successfully escaped {ename}\n")
                enemy_Hp = 0
            else:
                print(f"You failed to escap\n")
                print(f"Player takes: {enemy_dmg} and has {Player_Hp} HP left\n")
        #Interesting bug where the weapon doesn't change right away. 
        elif val2 == "change weapon":
            if Player_DMG == Player_DMGLG:
                Player_DMG == Player_DMGTor
            else:
                Player_DMG == Player_DMGLG
        elif val2 == "help":
            combat_help_file = open("mainMenuHelp.txt")
            file_contents = help_file.read()
            print(file_contents)
            
    with open("data.json", "r") as f:
        data = json.load(f)
    data['ship']['HP'] = Player_Hp
    write_to_json(data)

                
                    
                
            
                
                
            
combat_intro()
combat()
            
            
            
            
            
            
