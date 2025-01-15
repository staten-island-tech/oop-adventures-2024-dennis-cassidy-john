import pygame
from tilemap import TileMap
from module import Tilemap
# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TILE_SIZE = 32  # Size of each tile in pixels

class SpriteSheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert_alpha()

    def parse_sprite(self, name):
        # Placeholder: Should return a specific tile image
        return self.spritesheet

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tile Map Viewer")
    clock = pygame.time.Clock()

    # Load resources
    spritesheet = SpriteSheet("tile_spritesheet.png")  # Replace with your spritesheet file
    tilemap = TileMap("map.csv", spritesheet, TILE_SIZE)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the tile map
        tilemap.draw_map(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()