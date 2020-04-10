# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = [] if inventory is None else inventory
        self.light = False

    def __str__(self):
        room_items = [x.name for x in self.current_room.has_items] 
        
        if len(self.current_room.has_items) < 1:
            return (f' \n You are currently at the {self.current_room.name} \
                    \n {self.current_room.description} \
                    \n You see no items in the room. ')
        else:
            return (f' \n You are currently at the {self.current_room.name} \
                    \n {self.current_room.description}\
                    \n You see the following items: \
                    \n {room_items}')

    def item__str__(self):
            return (f'\n **{self.current_room.has_items.description}**')

    def inv__str__(self):
        print (f'****Inventory****')
        inv = [x.name for x in self.inventory] 
        print(inv)
        return '*****************'
            
    def move(self, direction):

        if self.current_room.light_required == False or self.light == True:
            new_room = getattr(self.current_room, f'{direction}_to')
            if new_room == None:
                print('You cannot go that way. Please choose another direction')
            elif new_room is not None:
                self.current_room = new_room
        
        else:
            print('As you continue down this hallway without a light, everything around you turns pitch black. You are unable to navigate your way through the cave.')
            print('Press Q to restart')
            
            
            
            

    def take_item(self, item):
        item_taken = False
        for x in self.current_room.has_items:
            if x.name == item:
                self.inventory.append(x)
                self.current_room.has_items.remove(x)
                print(f'You have taken the item: {x.name}.')
                item_taken = True
        if item_taken == False:
            print("That item is not in the room")
            


    def drop_item(self, item): 
        item_dropped = False
        for x in self.inventory:
            if x.name == item:
                self.current_room.has_items.append(x)
                self.inventory.remove(x)
                print(f'You have dropped the {x.name} in the {self.current_room.name}')
                item_dropped = True
        if item_dropped == False:
            print('You do not have that item in your inventory.')


        

        

        