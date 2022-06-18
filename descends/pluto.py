import time
locations = {'Landing Zone': {'name': 'Landing Zone', 'S': 'Pirate Hideout', 'N': 'Pirate Hideout', 'W': 'Endless Tundra', 'E': 'Endless Tundra'},
             'Pirate Hideout': {'name': 'Pirate Hideout', 'N': 'Landing Zone', 'S': 'Landing Zone'},
             'Endless Tundra': {'name': 'Endless Tundra', 'W': 'Landing Zone', 'E': 'Landing Zone'}
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
