locations = {'Landing Zone': {'name': 'Landing Zone', 'S': 'Uranium Fields', 'N': 'Uranium Fields', },
     'Uranium Fields': {'name': 'Uranium Fields', 'S': 'Landing Zone'}
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
