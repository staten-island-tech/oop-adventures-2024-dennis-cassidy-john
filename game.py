import pygame
import sys


pygame.init()
tile_size = 16
cols, rows = 20, 16
screen_width = cols * tile_size

screen_height = rows * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('collect the items')



omar_image = pygame.image.load('omar.png')  
omar_image = pygame.transform.scale(omar_image, (tile_size, tile_size))    
water_image = pygame.image.load('water.png')
water_image = pygame.transform.scale(water_image, (tile_size, tile_size))
camel_image = pygame.image.load('camel.png')
camel_image = pygame.transform.scale(camel_image, (tile_size, tile_size))
font = pygame.font.Font(None, 24)  
game_over_font = pygame.font.Font(None, 36)  
clock = pygame.time.Clock()



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

    def obstacle(self, cactus):
        if self.x == cactus.x and self.y == cactus.y:
            self.health -= 20  
            return True
        return False
        
    def water(self, water):
        if self.x == water.x and self.y == water.y:
            self.health += 5
            if self.health > self.max_health:
                self.health = self.max_health
            return True
        return False
    
    def draw(self):
        screen.blit(self.image, (self.x * tile_size, self.y * tile_size))   
class water:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = water_image
    def draw(self):
        screen.blit(self.image, (self.x * tile_size, self.y * tile_size))
class camel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = camel_image 
         
    def draw(self):
        screen.blit(self.image, (self.x * tile_size, self.y * tile_size))
class Game:
    def __init__(self):
        self.omar = Omar(5, 5, 100)  
        self.cacti = [Cactus(8, 8), Cactus(12, 6), Cactus(3, 10)]  
        self.water = [water(15,1), water (12,12), water (5,2)]
        self.countdown_time = 60  
        self.start_ticks = pygame.time.get_ticks()  
        self.game_over = False
        self.victory = False  
    def check_interactions(self):       
        for water in self.water:
            if self.omar.x == water.x and self.omar.y == water.y:
                self.water.remove(water)  
        for camel in self.camel:
            if self.omar.x == camel.x and self.omar.y == camel.y:
                self.camel.remove(camel) 
        
        if len(self.water) == 0 and len(self.camel) == 0:
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
    
    def draw_game(self):
        screen.fill((255, 255, 255))  
        
        for water_tile in self.water:
            water_tile.draw()
        
        for camel_tile in self.camel:
            camel_tile.draw()
        self.omar.draw()
        timer_text = font.render(f"Time: {self.remaining_time}s", True, (0, 0, 0))
        screen.blit(timer_text, (10, 10))
    def display_game_over(self, message):
        screen.fill((255, 255, 255))  
        game_over_text = game_over_font.render(message, True, (255, 0, 0))  
        screen.blit(game_over_text, (screen_width // 4, screen_height // 3)) 
        pygame.display.update()
if __name__ == "__main__":
    game = Game()
    game.run()