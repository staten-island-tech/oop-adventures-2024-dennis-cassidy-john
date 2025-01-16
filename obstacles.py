class Obstacles():
    def __init__(self, quicksand, cactus):
        self.quicksand = quicksand
        self.cactus = cactus
    def __str__(self):
        return f"{self.cactus}, {self.quicksand}"
    
    def do_damage(self, player, damage):
        player['health'] -= damage
        if player['health'] < 0: 
            player['health'] = 0
        print(f"Player health is now {player['health']}")
    
    def cactus_damage(self, player):
        self.do_damage(player, self.cactus)
    
    def quicksand_damage(self, player):
        self.do_damage(player, self.quicksand)
        
obstacle = Obstacles(cactus= 10, quicksand = 10)
player = {'health':100}

obstacle.cactus_damage(player)
obstacle.quicksand_damage(player)
obstacle.quicksand_damage(player)