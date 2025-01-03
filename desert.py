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

# Load images (Replace with your actual file paths)
sand_img = pygame.image.load('sand.png').convert_alpha()  # Load sand image with transparency
cactus_img = pygame.image.load('cactus.png').convert_alpha()  # Load cactus image with transparency
camel_img = pygame.image.load('camel.png').convert_alpha()  # Load camel image with transparency

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
                # Manually assign tiles for the demo (no random generation)
                if row % 3 == 0:
                    map_row.append(sand_img)  # Every 3rd row is sand
                elif row % 3 == 1:
                    map_row.append(cactus_img)  # Every 2nd row has cactus
                else:
                    map_row.append(sand_img)  # Default to sand
            map_grid.append(map_row)
        return map_grid

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
        self.image = pygame.image.load('omar.png').convert_alpha()  # Load player image
        self.rect = self.image.get_rect()  # Get the rectangle of the image for positioning

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.topleft = (self.x * TILE_SIZE, self.y * TILE_SIZE)  # Update player position

    def draw(self):
        SCREEN.blit(self.image, self.rect)  # Draw the player image at the correct position

# Initialize Desert Map
desert_map = DesertMap(SCREEN_WIDTH // TILE_SIZE, SCREEN_HEIGHT // TILE_SIZE)

# Initialize Player
omar = Player(5, 5)  # Start the player at position (5, 5)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    SCREEN.fill((255, 255, 255))  # Clear the screen (white background)
    
    # Draw the map
    desert_map.draw()
    
    # Draw the player
    omar.draw()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement (simple WASD control)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        omar.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        omar.move(1, 0)
    if keys[pygame.K_UP]:
        omar.move(0, -1)
    if keys[pygame.K_DOWN]:
        omar.move(0, 1)

    # Update the display
    pygame.display.update()

    # Set the FPS
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()

