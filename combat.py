from Ship import Ship
from Monster import *
import time 
import random
import json
from navigation import *

def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)

# def return_key(destination):
#     for key, value in solar_system.items():
#         if key==destination:
#             return int(value)
#     return('Key Not Found')

def combat_intro(Monster):
    print(f"You encounter an enemy. It's {Monster.name}!")
    answer = input("Do you wish to try and flee?\n").lower()
    if (answer == "flee") or (answer == "yes"):
        time.sleep(3)
        print("Successfully Fled")
    else:
        print("Get ready for combat!\n")
        combat(Monster)

def combat(Monster): 
    enemy_Hp = Monster.Hp
    enemy_dmg = Monster.Dmg
    Player_DMG = Ship.Weapons["LG"]
    print(f"{Monster.name} is approaching the your ship, ready to attack\n")
    print("How do you proceed? \n")
    while enemy_Hp > 0:
        action = input("Shoot | Flee | Change Weapon\n").lower()
        if action == "shoot":
            if Player_DMG == Ship.Weapons["Tor"]:
                if Ship.Resources["torpedo"] > 0:
                    Ship.Resources["torpedo"] -= 1
                else:
                    print("out of Torpedoes :(\nswitching back to Laser Gun :)")
                    Player_DMG = Ship.Weapons["LG"]
            TotalDmg = Player_DMG + random.randint(0, 5)
            enemy_Hp = enemy_Hp - TotalDmg
            if enemy_Hp <= 0:
                prize = random.choice(list(Ship.Resources))
                prize_amt = random.randint(1,3)
                Ship.Resources[prize] += prize_amt
                print(f"You dealt {TotalDmg} damage, defeating {Monster.name}, and took {prize_amt} {prize} they dropped\n")
                quit()
            print(f"You inflicted {TotalDmg} damage, and your enemy has {enemy_Hp} remaining HP.")
            Ship.HP = Ship.HP - enemy_dmg
            print("Your enemy fires back!")
            if Ship.HP <= 0:
                print(f"Your ship has been destroyed! Game over, loser\n")
                exit()
            else:
                print(f"You've been dealt {enemy_dmg} damage, and you have {Ship.HP} HP left \n")

        elif action == "flee":
            player_Flee = random.randint(1,100)
            enemy_Flee = random.randint(1,100)
            if player_Flee > enemy_Flee:
                print(f"You have successfully escaped {ename}\n")
                enemy_Hp = 0
            else:
                print(f"You failed to escape, and were hit")
                Ship.HP = Ship.HP - enemy_dmg
                print(f"You've been dealt {enemy_dmg} damage, and you have {Ship.HP} HP left \n")
        #Interesting bug where the weapon doesn't change right away. 
        elif action == "change weapon":
            if Player_DMG == Ship.Weapons["LG"]:
                Player_DMG = Ship.Weapons["Tor"]
                print("Switched to Torpedo\n")
            else:
                Player_DMG = Ship.Weapons["LG"]
                print("Switched to Laser Gun\n")
        elif action == "help":
            combat_help_file = open("combatHelp.txt")
            file_contents = combat_help_file.read()
            print(file_contents)        
    # with open("data.json", "r") as f:
    # data = json.load(f)
    # data['ship']['HP'] = Player_Hp
    # write_to_json(data)
            
combat_intro(Alien)
            
            
            
            
