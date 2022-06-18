from Ship import Ship
import Monster
import time 
import random
import json

# Player Variables

Player_DMGLG = Ship.Inventory["LG"]
Player_DMGTor = Ship.Inventory["Tor"]
Player_DMG = Player_DMGLG

# Enemy Variables
# global enemy_dmg 
# enemy_dmg= 2

def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)

# def return_key(destination):
#     for key, value in solar_system.items():
#         if key==destination:
#             return int(value)
#     return('Key Not Found')

def combat_intro():
    print("You encounter an enemy!")
    answer = input("Do you wish to try and flee?\n").lower()
    if (answer == "flee") or (answer == "yes"):
        time.sleep(3)
        print("Successfully Fled")
        return
    else:
        print("Get ready for combat!\n")

class Alien_Queen:
    enemy_name = "Alien Queen"
    enemy_Hp = 1000
    enemy_dmg = 10

def combat (enemy_name, enemy_Hp, enemy_dmg):
    with open("data.json", "r") as f:
        data = json.load(f)
    Player_Hp = data['ship']['HP'] 
    # ename = enemy_name
    # enemy_Hp = 20
    print(f"{enemy_name} is approaching your ship, ready to attack")
    print("How do you proceeed? ")
    while enemy_Hp > 0:
        action = input("Shoot | Flee | Change Weapon\n").lower()
        if action == "shoot":
            dmgtoe = Player_DMG + random.randint(0, 9)
            enemy_Hp = enemy_Hp - dmgtoe
            print(f"you inflict {dmgtoe} damage, and your enemy has {enemy_Hp} HP left. \n")
            if enemy_Hp <= 0:
                prize = random.choice(list(Ship.Resources))
                prize_amt = random.randint(1,3)
                Ship.Resources[prize] += prize_amt
                print(f"You have defeated the {enemy_name}, and took {prize_amt} {prize} they dropped\n")
                return
            Player_Hp = Player_Hp - enemy_dmg
            if Player_Hp <= 0:
                print(f"Your ship has been destroyed! Game over\n")
                exit()
            print(f"Your ship takes {enemy_dmg} damage, and has {Player_Hp} HP left. \n")
        elif action == "flee":
            player_Flee = random.randint(1,100)
            enemy_Flee = random.randint(1,100)
            if player_Flee > enemy_Flee:
                print(f"You have successfully escaped {enemy_name}\n")
                enemy_Hp = 0
            else:
                print(f"You failed to escape\n")
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

    
# # combat_intro()
# combat(Monster.Alien_Queen.enemy_name, Monster.Alien_Queen.enemy_Hp, Monster.Alien_Queen.enemy_dmg)
# combat(Alien_Queen.enemy_name, Alien_Queen.enemy_Hp, Alien_Queen.enemy_dmg)
# combat(Alien_Queen.enemy_name, Alien_Queen.enemy_Hp, Alien_Queen.enemy_dmg)
# combat(Alien_Queen.enemy_name, Alien_Queen.enemy_Hp, Alien_Queen.enemy_dmg)

            
            
            
            
            
            
