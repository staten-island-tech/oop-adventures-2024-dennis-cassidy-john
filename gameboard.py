class Gameboard():
    def __init__(self, wall, tiles, start, finish):
        self.wall = wall
        self.tiles = tiles
        self.start = start
        self.finish = finish
    def __str__(self):
        return f"{self.wall}, {self.tiles}, {self.start}, {self.finish}"