from room import Room
from player import Player
from item import Item
from os import system, name
import sys
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                    ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    ),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                   ),
    'dark':   Room("Dark Passageway", """It's too dark to keep going. If only I had a light source.""",True),
    'ledge':  Room('The Ledge', """You can see goblins working down below. Better be quiet"""),


}

# item = {
#     'outside':  Item("Flaming Torch",
#                      "I can see deeper into the cave with this"),
# }

torch = Item('torch', 'I could see in the dark with this.')
towel = Item('towel', 'Dont forget a towel!')
map = Item('map', 'Could this be a treasure map?')
arrow = Item('broken arrow', 'A broken arrow.')
potion = Item('strange potion', 'I wonder what this does?')
ring = Item('ring', 'Could this be a precious?')

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['foyer'].w_to = room['dark']
room['dark'].e_to = room['foyer']
room['ledge'].n_to = room['dark']
room['dark'].s_to = room['ledge']

#
# Main
#

def clear(): 
    # for windows 
    _ = system('cls' if name == 'nt' else 'clear') 

# def start_game():
#     print(f'\n***** Welcome to Adventure Quest! *****')
#     print(f'\n[Q] -- Quit \n ')
# start_game()    
print("")
print("*************Adventure Quest!**********************")
print('---- Lets get started! -----')
player = Player(input('What is your name?'), room["outside"])    
cin = 'p'

""" OUTSIDE ROOM ITEMS """
room['outside'].has_items.append(torch)
room['outside'].has_items.append(map)  

""" FOYER ITEMS """
room['foyer'].has_items.append(towel) 

""" OVERLOOK ITEMS"""
room['overlook'].has_items.append(arrow)

"""NARROW ITEMS """
room['narrow'].has_items.append(potion)

"""TREASURE ROOM ITEMS """


"""DARK ROOM """



""" LEDGE ROOM ITEMS """
room['ledge'].has_items.append(ring)


while cin != 'q':     
    
    print(player.__str__())
    #1 create options to move
    #2 if correct option selected, move in that direction
    #3 if incorrect option, re prompt
    cin = input('''\n Which direction do you want to go? 
             \n           [N] - North    ----- [T] - Take Item
             \nWest - [W]  O  [E] - East ----- [I] - Inventory
             \n           [S] - South    ----- [D] - Drop Item
             \n                          ----- [L] - Inspect Item
             ''')
    
    
    if cin == 'n':
        player.move(cin)
        
        
        
    elif cin == 'e':
        player.move(cin)
        
        
        
    elif cin == 's':
        player.move(cin)
        
        
        
    elif cin == 'w':
        player.move(cin)
        

    elif cin == "i":
        clear()
        print('')
        print(player.inv__str__())
        cin = input('Press enter to return to the menu')

    elif cin == "t":
        clear()
        print(player.current_room.show_items())
        cin = input('What item do you want to take?')
        player.take_item(cin)
        
        

    elif cin == "l":
        clear()
        print('')
        print(player.item__str__())
        print('')
        cin = input('Press enter to return to the menu')

    elif cin == 'd':
        clear()
        print(player.inv__str__())
        cin = input('What item do you want to drop?') 
        player.drop_item(cin)
        
        
    # elif cin != 'g' or 'G':
    #         print('')
    #         print('Please press [S] to start the game or [Q] to quit the game.')   
    #         print(f'\n[G] -- Start Game \
    #                 \n[Q] -- Quit \n ')
    #         cin = input('') 
            
    
else:
    clear()
    print('You have quit the game')

        
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


