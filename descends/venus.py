locations = {'Landing Zone': {'name': 'Landing Zone', 'S': 'Aphrodites Channel', 'N': 'Aphrodites Channel', 'E':'Makeout Point', 'W':'Clamshell Cove' },
     'Clamshell Cove': {'name': 'Clamshell Cove', 'E': 'Landing Zone','W': 'Makeout Point'},
     'Aphrodites Channel': {'name': 'Aphrodites Channel', 'N': 'Landing Zone','S':'Landing Zone' },
     'Makeout Point': {'name': 'Makeout Point', 'W':'Landing Zone','E':'Clamshell Cove' }
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
      return
    # bad command
    else:
      print("Invalid Direction")
