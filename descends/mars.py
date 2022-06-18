import time
import json
from Ship import Ship
import random
locations = {'Landing Zone': {'name': 'Landing Zone', 'S': 'Great Dessert', 'N': 'Olympus Mons', },
     'Great Dessert': {'name': 'Great Dessert', 'E': 'Olympus Mons', 'N': 'Landing Zone', 'S': 'South Pole', 'W': 'Olympus Mons'},
     'South Pole': {'name': 'South Pole', 'N': 'Great Dessert', 'S':'Landing Zone' },
     'Olympus Mons': {'name': 'Olympus Mons', 'W':'Great Dessert','E':'Great Dessert'},
     }
Player_DMGLG = Ship.Inventory["LG"]
Player_DMGTor = Ship.Inventory["Tor"]
Player_DMG = Player_DMGLG

# Enemy Variables
# global enemy_dmg 
# enemy_dmg= 2

def write_to_json(data):
    with open("data.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)
class Alien:
    enemy_name = "Alien"
    enemy_Hp = 30
    enemy_dmg = 5

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
            player_dmg = random.randint(1,enemy_dmg)
            Player_Hp = Player_Hp - player_dmg
            if Player_Hp <= 0:
                print(f"Your ship has been destroyed! Game over\n")
                exit()
            print(f"Your ship takes {player_dmg} damage, and has {Player_Hp} HP left. \n")
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

def descend():
    directions = ['N', 'S', 'E', 'W']
    current_room = locations['Landing Zone']

    # game loop
    while True:
        # display current location
        print()
        print('You are in the {}.'.format(current_room['name']))

      # get user input
        command = input('\nWhat direction do you want to go? ').upper()
      # movement
        if command in directions:
            if command in current_room:
                if random.randint(1,5) == 5:
                  combat(Alien.enemy_name, Alien.enemy_Hp, Alien.enemy_dmg)
                current_room = locations[current_room[command]]
            else:
                # bad movement
                print("Desolate emptiness, best not head that way....")
      # Exit game
        elif command.lower() in ('leave'):
          print("Ascending....")  
          time.sleep(2)
          print("\n Welcome Back Cadet!")
          return
        
      # bad command
        else:
          print("Invalid Direction")
