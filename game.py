import pygame
import sys

<<<<<<< Updated upstream
pygame.init()

tile_size = 30
cols, rows = 20, 16
screen_width = cols * tile_size
screen_height = rows * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Move Omar One Tile at a Time on 20x16 Grid with Countdown Timer')


omar_image = pygame.image.load('omar.png')  
omar_image = pygame.transform.scale(omar_image, (tile_size, tile_size))  

cactus_image = pygame.image.load('cactus.png')  
cactus_image = pygame.transform.scale(cactus_image, (tile_size, tile_size))  

water_image = pygame.image.load('water.png')
water_image = pygame.transform.scale(water_image, (tile_size, tile_size))

font = pygame.font.Font(None, 36)  
game_over_font = pygame.font.Font(None, 72)  


clock = pygame.time.Clock()

class Omar:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.image = omar_image
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def obstacle(self, cactus):
        if self.x == cactus.x and self.y == cactus.y:
            self.health -= 20  
            return True
        return False
        
    def water(self, water):
        if self.x == water.x and self.y == water.y:
            self.health += 5
            return True
        return False
    
    def draw(self):
        screen.blit(self.image, (self.x * tile_size, self.y * tile_size))  

class Cactus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = cactus_image

    def draw(self):
        screen.blit(self.image, (self.x * tile_size, self.y * tile_size))  

class water:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = water_image

    def draw(self):
        screen.blit(self.image, (self.x * tile_size, self.y * tile_size))


class Game:
    def __init__(self):
        self.omar = Omar(5, 5)  
        self.cacti = [Cactus(8, 8), Cactus(12, 6), Cactus(3, 10)]  
        self.water = [water(15,1), water (12,12), water (5,2)]
        self.countdown_time = 60  
        self.start_ticks = pygame.time.get_ticks()  
        self.game_over = False

    def run(self):
        while True:
            if self.game_over:
                self.display_game_over()
                continue  
            self.handle_events()

            self.update_timer()

            self.check_interactions()  

            self.draw_game()

            pygame.display.update()  
            clock.tick(60)  

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not self.game_over:
                if event.key == pygame.K_LEFT:  
                    if self.omar.x > 0:
                        self.omar.move(-1, 0)
                if event.key == pygame.K_RIGHT: 
                    if self.omar.x < cols - 1:
                        self.omar.move(1, 0)
                if event.key == pygame.K_UP:  
                    if self.omar.y > 0:
                        self.omar.move(0, -1)
                if event.key == pygame.K_DOWN:  
                        self.omar.move(0, 1)

    def update_timer(self):
        elapsed_time = (pygame.time.get_ticks() - self.start_ticks) // 1000  
        self.remaining_time = self.countdown_time - elapsed_time
       
        if self.remaining_time <= 0:
            self.remaining_time = 0
            self.game_over = True  

    def check_interactions(self):
        for cactus in self.cacti: 
            if self.omar.obstacle(cactus):
                self.cacti.remove(cactus)  
                self.remaining_time -= 20
                if self.remaining_time < 0:
                    self.remaining_time = 0

        for water_tile in self.water:  
            if self.omar.water(water_tile):
                self.water.remove(water_tile)
                self.remaining_time += 8

    def draw_game(self):
        screen.fill((255, 255, 255))  

        for row in range(0, screen_height, tile_size):
            for col in range(0, screen_width, tile_size):
                pygame.draw.rect(screen, (200, 200, 200), (col, row, tile_size, tile_size), 1)

        for cactus in self.cacti:
            cactus.draw()
        
        for water_tile in self.water:
            water_tile.draw()

        self.omar.draw()

        timer_text = font.render(f"Time: {self.remaining_time}s", True, (0, 0, 0))
        screen.blit(timer_text, (10, 10))

        health_text = font.render(f"Health: {self.omar.health}", True, (0, 0, 0))
        screen.blit(health_text, (10, 50))

    def display_game_over(self):
        screen.fill((255, 255, 255))  
        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))  
        screen.blit(game_over_text, (screen_width // 4, screen_height // 3)) 
        pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
=======
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

>>>>>>> Stashed changes
