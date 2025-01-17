import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Quit Example")


tile_size = 16
cols, rows = 20, 16
screen_width = cols * tile_size
screen_height = rows * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collect the Items')

# Load images and fonts
omar_image = pygame.image.load('omar.png')
omar_image = pygame.transform.scale(omar_image, (tile_size, tile_size))
water_image = pygame.image.load('water.png')
water_image = pygame.transform.scale(water_image, (tile_size, tile_size))
camel_image = pygame.image.load('camel.png')
camel_image = pygame.transform.scale(camel_image, (tile_size, tile_size))
cactus_image = pygame.image.load('cactus.png')
cactus_image = pygame.transform.scale(cactus_image, (tile_size, tile_size))

font = pygame.font.Font(None, 24)
game_over_font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()



def generate_random_positions(count, exclude_positions=None):
    exclude_positions = exclude_positions or []
    positions = set()
    while len(positions) < count:
        x, y = random.randint(0, cols - 1), random.randint(0, rows - 1)
        if (x, y) not in exclude_positions:
            positions.add((x, y))
    return list(positions)



class Omar:
    def __init__(self, x, y, health, max_health=100):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
        self.image = omar_image

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        screen.blit(self.image, (self.x * tile_size, self.y * tile_size))


class Water:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = water_image

    def draw(self):
        screen.blit(self.image, (self.x * tile_size, self.y * tile_size))


class Camel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = camel_image

    def draw(self):
        screen.blit(self.image, (self.x * tile_size, self.y * tile_size))


class Cactus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = cactus_image

    def draw(self):
        screen.blit(self.image, (self.x * tile_size, self.y * tile_size))


class Game:
    def __init__(self):
        # Place Omar at a random position
        omar_position = generate_random_positions(1)[0]
        self.omar = Omar(*omar_position, 100)

        # Generate random positions for Cactus, Water, and Camel
        exclude_positions = [omar_position]
        cactus_positions = generate_random_positions(3, exclude_positions)
        water_positions = generate_random_positions(3, exclude_positions + cactus_positions)
        camel_positions = generate_random_positions(2, exclude_positions + cactus_positions + water_positions)

        # Initialize objects
        self.cacti = [Cactus(x, y) for x, y in cactus_positions]
        self.water = [Water(x, y) for x, y in water_positions]
        self.camels = [Camel(x, y) for x, y in camel_positions]

        self.countdown_time = 60
        self.start_ticks = pygame.time.get_ticks()
        self.game_over = False
        self.victory = False

    def check_interactions(self):
        for water_tile in self.water[:]:
            if self.omar.x == water_tile.x and self.omar.y == water_tile.y:
                self.water.remove(water_tile)

        for camel_tile in self.camels[:]:
            if self.omar.x == camel_tile.x and self.omar.y == camel_tile.y:
                self.camels.remove(camel_tile)

        for cactus in self.cacti:
            if self.omar.x == cactus.x and self.omar.y == cactus.y:
                self.omar.health -= 20
                if self.omar.health <= 0:
                    self.game_over = True

        if len(self.water) == 0 and len(self.camels) == 0:
            self.victory = True

    def run(self):
        while True:
            if self.game_over:
                self.display_game_over("Game Over")
                continue
            if self.victory:
                self.display_game_over("You Win!")
                continue
            self.handle_events()
            self.update_timer()
            self.check_interactions()
            self.draw_game()
            pygame.display.update()
            clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and not self.game_over and not self.victory:
                if event.key == pygame.K_LEFT and self.omar.x > 0:
                    self.omar.move(-1, 0)
                if event.key == pygame.K_RIGHT and self.omar.x < cols - 1:
                    self.omar.move(1, 0)
                if event.key == pygame.K_UP and self.omar.y > 0:
                    self.omar.move(0, -1)
                if event.key == pygame.K_DOWN and self.omar.y < rows - 1:
                    self.omar.move(0, 1)

    def update_timer(self):
        elapsed_time = (pygame.time.get_ticks() - self.start_ticks) // 1000
        self.remaining_time = self.countdown_time - elapsed_time

        if self.remaining_time <= 0:
            self.remaining_time = 0
            self.game_over = True

    def draw_game(self):
        screen.fill((255, 255, 255))

        for water_tile in self.water:
            water_tile.draw()

        for camel_tile in self.camels:
            camel_tile.draw()

        for cactus in self.cacti:
            cactus.draw()

        self.omar.draw()

        timer_text = font.render(f"Time: {self.remaining_time}s", True, (0, 0, 0))
        screen.blit(timer_text, (10, 10))

        health_text = font.render(f"Health: {self.omar.health}", True, (255, 0, 0))
        screen.blit(health_text, (10, 30))

    def display_game_over(self, message):
        screen.fill((255, 255, 255))
        game_over_text = game_over_font.render(message, True, (255, 0, 0))
        screen.blit(game_over_text, (screen_width // 4, screen_height // 3))
        pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()