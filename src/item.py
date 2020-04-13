class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Light(Item):
    def __init__(self):
        self.light = True


    