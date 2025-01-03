class Inventory:
    def __init__(self):
        self.items = [] 
        self.max_items = 10  
        
    def add_item(self, item):
        """Add an item to the inventory."""
        if len(self.items) < self.max_items:
            self.items.append(item)
        else:
            print("Inventory is full!")