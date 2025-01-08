class Player():
    def __init__(self, player, health, max_health=100):
        self.player = player
        self.health = health
        self.max_health = max_health
    def __str__(self):
        return f"{self.player}, {self.health}"

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.player} took {damage} damage! Health is now {self.health}/{self.max_health}.")

    def heal(self, water_bottle=100):
        self.health += water_bottle
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.player} healed {water_bottle} points! Health is now {self.health}/{self.max_health}.")

player = Player(player = "Omar", health=100)
print(player)

player.take_damage(10)

player.heal(100)

