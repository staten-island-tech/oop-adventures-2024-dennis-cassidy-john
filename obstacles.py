class Obstacles():
    def __init__(self, quicksand, cactus):
        self.quicksand = quicksand
        self.cactus = cactus
    def __str__(self):
        return f"{self.quicksand}, {self.cactus}" 