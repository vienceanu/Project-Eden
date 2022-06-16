rooms = {'Landing Zone': {'name': 'Landing Zone', 'South': 'Moon Core', 'North': 'Mineral Deposit 1', },
     'Moon Core': {'name': 'Moon Core', 'East': 'Crater Tycho', 'North': 'Landing Zone', 'South': 'Mineral DEpository', 'West': 'Crater Tycho'},
     'Cellar': {'name': 'Cellar', 'West': 'Bedroom'},
     'Library': {'name': 'Library', 'East': 'Landing Zone'},
     'Kitchen': {'name': 'Kitchen', 'West': 'Landing Zone', 'North': 'Dining Room'},
     'Dining Room': {'name': 'Dining Room', 'South': 'Kitchen'},
     'Dungeon': {'name': 'Dungeon', 'South': 'Landing Zone', 'East': 'Gallery'},
     'Gallery': {'name': 'Gallery', 'West': 'Dungeon'},
     }
directions = ['North', 'South', 'East', 'West']
current_room = rooms['Landing Zone']

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
            current_room = rooms[current_room[command]]
        else:
        # bad movement
            print("You can't go that way.")
  # Exit game
    elif command.lower() in ('q', 'quit'):
        break
  # bad command
    else:
        print("I don't understand that command.")