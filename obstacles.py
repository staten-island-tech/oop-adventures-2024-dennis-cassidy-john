class Obstacles():
    def __init__(self, cactus, quicksand, damage):
        self.cactus = cactus
        self.quicksand = quicksand
        self.damage = damage
    def __str__(self):
        return f"{self.cactus}, {self.quicksand}"
    def do_damage(self, player):
        player.health = player.health - self.damage
        print(f'Player health is now {player.health}')
    def cactus_damage():
        cactus.do_damage(player)
        
player = {'health':100}