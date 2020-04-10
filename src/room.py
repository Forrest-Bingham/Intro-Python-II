# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, light_required=False): #, has_items=None
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.has_items = []
        self.light_required = light_required
        # self.has_items = [] if has_items is None else has_items

    def show_items(self):
        y = [x.name for x in self.has_items] 
        return(y)
    