from Ship import Ship
import Monster
import time 
import random 


global Player_Hp 
Player_Hp = 50

global Player_DMG 
Player_DMG= 2

global ename 
ename = "Pirate"

global enemy_dmg 
enemy_dmg= 2

global dmgtoe 
dmgtoe= 0


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
        print("Get ready for combat!")

def combat ():
    global enemy_Hp 
    enemy_Hp = 20
    print(f" {ename} has approached the ship. it readies its weapons\n")
    while enemy_Hp > 0:
        val2 = input("How do you proceeed? (Shoot or Flee)\n")
        if val2 =="Shoot":
            dmgtoe = Player_DMG + random.randint(0, 9)
            print(f"Enemy takes {dmgtoe}")
            enemy_Hp = enemy_Hp - dmgtoe
            print(f"enemy health = {enemy_Hp}")
            print(f"Player takes: {enemy_dmg} and has {Player_Hp} HP left")
            
combat_intro()
combat()
            
            
            
            
            
            