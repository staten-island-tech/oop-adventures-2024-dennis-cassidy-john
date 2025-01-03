import pygame
import sys

pygame.init()

tile_size = 16  
cols, rows = 20, 16
screen_width = cols * tile_size
screen_height = rows * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Move Omar One Tile at a Time on 20x16 Grid with Countdown Timer')


omar_image = pygame.image.load('omar.png')  
omar_image = pygame.transform.scale(omar_image, (tile_size, tile_size))  

cactus_image = pygame.image.load('cactus.png')  
cactus_image = pygame.transform.scale(cactus_image, (tile_size, tile_size))  


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

    def check_collision(self, cactus):
        if self.x == cactus.x and self.y == cactus.y:
            self.health -= 20  
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

class Game:
    def __init__(self):
        self.omar = Omar(5, 5)  
        self.cacti = [Cactus(8, 8), Cactus(12, 6), Cactus(3, 10)]  
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
            self.check_collisions()

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

    def check_collisions(self):
        for cactus in self.cacti:
            if self.omar.check_collision(cactus):
                self.cacti.remove(cactus)  

        if self.omar.health <= 0:
            self.game_over = True  

    def draw_game(self):
        screen.fill((255, 255, 255))  

        for row in range(0, screen_height, tile_size):
            for col in range(0, screen_width, tile_size):
                pygame.draw.rect(screen, (200, 200, 200), (col, row, tile_size, tile_size), 1)

        for cactus in self.cacti:
            cactus.draw()

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
