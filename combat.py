from Ship import Ship
import Monster
import time 
import random
import json
import navigation

# Player Variables
global Player_Hp 
global Player_DMG 
Player_Hp = 50
Player_DMGLG = Ship.Inventory["LG"]
Player_DMGTor = Ship.Inventory["Tor"]
Player_DMG = Player_DMGLG

# Enemy Variables
global ename 
ename = "Pirate"
global enemy_dmg 
enemy_dmg= 2

#Damage to Enemy Variable. 
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
    answer = input("do you wish to try and flee?")
    if (answer.lower() == "flee") or (answer == "yes"):
        time.sleep(3)
        print("Successfully Fled")
    else:
        print("Get ready for combat!\n")

def combat ():
    global enemy_Hp 
    enemy_Hp = 20
    print(f" {ename} has approached the ship. it readies its weapons\n")
    print("How do you proceeed? \n")
    while enemy_Hp > 0:
        action = input("Shoot | Flee | Change Weapon\n").lower()
        if action =="shoot":
            dmgtoe = Player_DMG + random.randint(0, 9)
            print(f"Enemy takes {dmgtoe} damage. \n")
            enemy_Hp = enemy_Hp - dmgtoe
            if enemy_Hp < 0:
                print(f"you have defeated the {ename}")
                # enemy drop resource
                navigation_mode()
            print(f"enemy health = {enemy_Hp}\n")
            print(f"Player takes: {enemy_dmg}damage and has {Player_Hp} HP left\n")
        elif action == "flee":
            player_Flee = random.randint(1,100)
            enemy_Flee = random.randint(1,100)
            if player_Flee > enemy_Flee:
                print(f"You have successfully escaped {ename}\n")
                enemy_Hp = 0
            else:
                print(f"You failed to escape\n")
                print(f"Player takes: {enemy_dmg} and has {Player_Hp} HP left\n")
        #Interesting bug where the weapon doesn't change right away. 
        elif action == "change weapon":
            if Player_DMG == Player_DMGLG:
                Player_DMG == Player_DMGTor
                print("Switched to Torpedo\n")
            else:
                Player_DMG == Player_DMGLG
                print("Switched to Laser Gun\n")
        elif action == "help":
            combat_help_file = open("combatHelp.txt")
            file_contents = combat_help_file.read()
            print(file_contents)
            
    with open("data.json", "r") as f:
        data = json.load(f)
    data['ship']['HP'] = Player_Hp
    write_to_json(data)

                
                    
                
            
                
                
            
combat_intro()
combat()
            
            
            
            
            
            
