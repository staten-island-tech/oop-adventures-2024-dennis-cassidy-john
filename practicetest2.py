class Grocery():
    def __init__(self, inventory, customer):
        self.inventory = inventory
        self.customer = customer
    def buy_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{self.customer} just bought {item}")
        else:
            print("Item not in inventory")

inventory = ["apples", "bananas", "oranges", "broccoli"]
grocery_store = Grocery(inventory, "Dennis")
grocery_store.buy_item("apples")
grocery_store.buy_item("fdasfdasf")