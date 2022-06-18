import time
locations = {'Landing Zone': {'name': 'Landing Zone', 'S': 'Great Dessert', 'N': 'Olympus Mons', },
     'Great Dessert': {'name': 'Great Dessert', 'E': 'Olympus Mons', 'N': 'Landing Zone', 'S': 'South Pole', 'W': 'Olympus Mons'},
     'South Pole': {'name': 'South Pole', 'N': 'Great Dessert', 'S':'Landing Zone' },
     'Olympus Mons': {'name': 'Olympus Mons', 'W':'Great Dessert','E':'Great Dessert'},
     }

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
