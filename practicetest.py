class Store():
    def __init__(self, inventory, merchant):
        self.inventory = inventory
        self.merchant = merchant
    
    def buy(self, buyer, item):
        if item in inventory:
            return f"{buyer} just bought {item}"

inventory = {"apple", "banana", "orange"}
store = Store(inventory, "Jon the Merchant")
print(store.buy("Dennis", "apple"))