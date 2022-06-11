from Ship import Ship
import Monster
import time 
import random 


global Player_Hp 
Player_Hp = 50

global Player_DMG 
Player_DMG = 2

global ename 
ename = "Pirate"

global enemy_dmg 
enemy_dmg = 2

global dmgtoe 
dmgtoe = 0


# def return_key(destination):
#     for key, value in solar_system.items():
#         if key==destination:
#             return int(value)
#     return('Key Not Found')

def combat_intro(Ship):
    print("You encounter an enemy")
    val1 = input("will you fight or flee? \n")
    if val1.lower() == "flee":
        time.sleep(2)
        print("Succesfully Fled")
        # exit here to nav?
    else:
        print("Get ready for combat!")
        combat(Ship)

def combat (Ship):
    global enemy_Hp 
    Player_Hp = Ship.getHp()
    enemy_Hp = 20
    print(f"The {ename} has approached the ship and is about to attack\n")
    while enemy_Hp > 0 and Player_Hp > 0:
        val2 = input("How do you proceed? (Shoot or Flee)\n")
        if val2.lower() == "shoot":
            dmgtoe = Player_DMG + random.randint(0, 9)
            print(f"Enemy takes {dmgtoe} damage,")
            enemy_Hp = enemy_Hp - dmgtoe
            print(f"and has {enemy_Hp} HP left")
            
            Player_Hp = Player_Hp - enemy_dmg
            print(f"Your enemy returns fire. Your ship takes: {enemy_dmg} damage and has {Player_Hp} HP left")   
        if val2.lower() == "flee":
            time.sleep(2)
            print("Succesfully Fled")
        # exit here to nav.py?

s = Ship()
combat_intro(s)
#combat()
            
            
            
            
            
            