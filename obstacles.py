class Obstacles():
    def __init__(self, quicksand, cactus):
        self.quicksand = quicksand
        self.cactus = cactus
    def __str__(self):
<<<<<<< Updated upstream
        return f"{self.quicksand}, {self.cactus}" 
=======
        return f"{self.cactus}, {self.quicksand}"
    def do_damage(self, player):
        player['health'] -= self.damage
        if player['health'] < 0: 
            player['health'] = 0
        print(f'Player health is now {player['health']}')
    def cactus_damage(self, player):
        self.do_damage(player)
    def quicksand_damage(self, player):
        self.do_damage(player)
        
obstacle = Obstacles("cactus", "quicksand", 10)
player = {'health':100}

obstacle.cactus_damage(player)
obstacle.quicksand_damage(player)
>>>>>>> Stashed changes
