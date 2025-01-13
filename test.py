import csv

# Open the CSV file in read mode
with open('tilemap.tmx', 'r') as csvfile:
  # Create a reader object
  csv_reader = csv.reader(csvfile)
  
  # Iterate through the rows in the CSV file
  for row in csv_reader:
    # Access each element in the row
    print(row)


import pygame
import csv

# Constants
TILE_SIZE = 16  
SCREEN_WIDTH = 208 
SCREEN_HEIGHT = 96

def load_csv(filename):
    data = []
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    data.append([int(value) for value in row])


def load_tiles_from_spritesheet(spritesheet_path, tile_width, tile_height):
    spritesheet = pygame.image.load("SpriteSheet.png").convert_alpha()
    sheet_width, sheet_height = spritesheet.get_size()

    tiles = {}
    tile_id = 1  # Start tile ID at 1

    for y in range(0, sheet_height, tile_height):
        for x in range(0, sheet_width, tile_width):
            # Extract the tile as a subsurface
            tile = spritesheet.subsurface((x, y, tile_width, tile_height))
            tiles[tile_id] = tile
            tile_id += 1

    return tiles

# Draw the tile map
def draw_tilemap(screen, tilemap, tile_images):
    for row_index, row in enumerate(tilemap):
        for col_index, tile_id in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            if tile_id in tile_images:
                screen.blit(tile_images[tile_id], (x, y))

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tile Map Example")
    clock = pygame.time.Clock()

    # Load the tilemap and tiles from spritesheet
    tilemap = load_csv("tilemap.tmx")
    tile_images = load_tiles_from_spritesheet("spritesheet.png", TILE_SIZE, TILE_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen
        draw_tilemap(screen, tilemap, tile_images)  # Draw the tilemap

        pygame.display.flip()
        clock.tick(60)  # Cap the frame rate

    pygame.quit()

if __name__ == "__main__":
    main()