import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32  # Size of each tile (32x32 pixels)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Desert Map")

# Colors
WHITE = (255, 255, 255)
SAND_COLOR = (255, 223, 127)
CACTUS_COLOR = (34, 139, 34)
ROCK_COLOR = (169, 169, 169)

# Load images (if you have desert-themed images, you can load them here)
sand_img = pygame.Surface((TILE_SIZE, TILE_SIZE))
sand_img.fill(SAND_COLOR)  # Sand tile (just a colored surface here for simplicity)

cactus_img = pygame.Surface((TILE_SIZE, TILE_SIZE))
cactus_img.fill(CACTUS_COLOR)  # Cactus tile (colored surface for simplicity)

rock_img = pygame.Surface((TILE_SIZE, TILE_SIZE))
rock_img.fill(ROCK_COLOR)  # Rock tile (colored surface)

# Define the Map
class DesertMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = self.generate_map()

    def generate_map(self):
        # Generate a simple desert map (a grid of tiles)
        map_grid = []
        for row in range(self.height):
            map_row = []
            for col in range(self.width):
                # Randomly assign different tiles for variety
                tile = self.get_random_tile()
                map_row.append(tile)
            map_grid.append(map_row)
        return map_grid

    def get_random_tile(self):
        # Randomly choose a tile (sand, cactus, or rock)
        import random
        tile_choice = random.choice([sand_img, cactus_img, rock_img])
        return tile_choice

    def draw(self):
        # Draw all the tiles on the screen
        for row in range(self.height):
            for col in range(self.width):
                tile = self.map[row][col]
                SCREEN.blit(tile, (col * TILE_SIZE, row * TILE_SIZE))

# Player Class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((0, 0, 255))  # Blue color for the player

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        SCREEN.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))

# Initialize Desert Map
desert_map = DesertMap(SCREEN_WIDTH // TILE_SIZE, SCREEN_HEIGHT // TILE_SIZE)

# Initialize Player
player = Player(5, 5)  # Start the player at position (5, 5)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    SCREEN.fill(WHITE)  # Clear the screen
    
    # Draw the map
    desert_map.draw()
    
    # Draw the player
    player.draw()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement (simple WASD control)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        player.move(1, 0)
    if keys[pygame.K_UP]:
        player.move(0, -1)
    if keys[pygame.K_DOWN]:
        player.move(0, 1)

    # Update the display
    pygame.display.update()

    # Set the FPS
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
