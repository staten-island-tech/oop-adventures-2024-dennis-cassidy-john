import pygame
import csv

# Constants
TILE_SIZE = 16  
SCREEN_WIDTH = 208 
SCREEN_HEIGHT = 96

# Function to load CSV data (tilemap layers)
def load_csv_layers(filenames):
    layers = []
    for filename in filenames:
        data = []
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    try:
                        # Convert each value to integer, corresponding to tile IDs
                        data.append([int(value) for value in row])
                    except ValueError:
                        print(f"Warning: Invalid value in row of {filename}. Replacing with 0.")
                        data.append([0 for _ in row])  # Replace invalid data with 0
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
        layers.append(data)
    return layers


# Function to load tiles from a sprite sheet
def load_tiles_from_spritesheet(spritesheet_path, tile_width, tile_height):
    spritesheet = pygame.image.load(spritesheet_path).convert_alpha()
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

# Draw the tile map layers in the Pygame window
def draw_tilemap(screen, layers, tile_images):
    for layer in layers:
        for row_index, row in enumerate(layer):
            for col_index, tile_id in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if tile_id in tile_images:
                    screen.blit(tile_images[tile_id], (x, y))

# Main function to run the Pygame program
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tile Map Example")
    clock = pygame.time.Clock()

    # Load the tilemap layers (each file corresponds to a different layer)
    filenames = ['layer1.csv', 'layer2.csv', 'layer3.csv']  # Replace with actual layer file paths
    layers = load_csv_layers(filenames)

    # Load tiles from the sprite sheet
    tile_images = load_tiles_from_spritesheet("spritesheet.png", TILE_SIZE, TILE_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen before drawing new frame
        screen.fill((0, 0, 0))  # Clear with black background

        # Draw the tilemap layers
        draw_tilemap(screen, layers, tile_images)

        pygame.display.flip()
        clock.tick(60)  # Cap the frame rate to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()