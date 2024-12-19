class Player():
    def __init__(self, player, health):
        self.player = player
        self.health = health
    def __str__(self):
        return f"{self.player}, {self.health}"

