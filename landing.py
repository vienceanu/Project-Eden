locations = {'Landing Zone': {'name': 'Landing Zone', 'S': 'Moon Core', 'N': 'Mineral Deposit 1', },
     'Moon Core': {'name': 'Moon Core', 'E': 'Crater Tycho', 'N': 'Landing Zone', 'S': 'Mineral Depository', 'W': 'Crater Tycho'},
     'Crater Tycho': {'name': 'Crater Tycho', 'N': 'Pirate Base', 'W':'Moon Core','E':'Moon Core','S':'Pirate Base' },
     'Pirate Base': {'name': 'Pirate Base', 'N': 'Crater Tycho', 'W':'Mineral Deposit 1','E':'Mineral Deposit 1','S':'Crater Tycho' },
     'Mineral Deposit 1': {'name': 'Mineral Deposit 1', 'N': 'Moon Core', 'W':'Pirate Base','E':'Pirate Base','S':'Landing Zone' }
     }
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
    elif command.lower() in ('q', 'quit'):
        break
  # bad command
    else:
        print("I don't understand that command.")