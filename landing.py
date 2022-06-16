locations = {'Landing Zone': {'name': 'Landing Zone', 'South': 'Moon Core', 'North': 'Mineral Deposit 1', },
     'Moon Core': {'name': 'Moon Core', 'East': 'Crater Tycho', 'North': 'Landing Zone', 'South': 'Mineral Depository', 'West': 'Crater Tycho'},
     'Crater Tycho': {'name': 'Crater Tycho', 'North': 'Pirate Base', 'West':'Moon Core','East':'Moon Core','South':'Pirate Base' },
     'Pirate Base': {'name': 'Pirate Base', 'North': 'Crater Tycho', 'West':'Mineral Deposit 1','East':'Mineral Deposit 1','South':'Crater Tycho' },
     'Mineral Deposit 1': {'name': 'Mineral Deposit 1', 'North': 'Moon Core', 'West':'Pirate Base','East':'Pirate Base','South':'Landing Zone' }
     }
directions = ['North', 'South', 'East', 'West']
current_room = locations['Landing Zone']

# game loop
while True:
    # display current location
    print()
    print('You are in the {}.'.format(current_room['name']))

  # get user input
    command = input('\nWhat direction do you want to go? ').strip()
  # movement
    if command in directions:
        if command in current_room:
            current_room = locations[current_room[command]]
        else:
        # bad movement
            print("You can't go that way.")
  # Exit game
    elif command.lower() in ('q', 'quit'):
        break
  # bad command
    else:
        print("I don't understand that command.")