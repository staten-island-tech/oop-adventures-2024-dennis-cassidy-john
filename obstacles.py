class Obstacles():
    def __init__(self, cactus, quicksand, damage):
        self.cactus = cactus
        self.quicksand = quicksand
        self.damage = damage
    def __str__(self):
        return f"{self.cactus}, {self.quicksand}"
    def do_damage(self, player):
        player['health'] -= self.damage
        print(f'Player health is now {player.health}')
    def cactus_damage(self, player):
        self.do_damage(player)
    def quicksand_damage(self, player):
        self.do_damage(player)
        
obstacle = Obstacles("cactus", "quicksand", 10)
player = {'health':100}
obstacle.cactus_damage(player)
obstacle.quicksand_damage(player)