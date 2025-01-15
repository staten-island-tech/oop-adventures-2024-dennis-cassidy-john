import pygame
import xml.etree.ElementTree as ET
import PIL
# Constants
TILE_SIZE = 16  
SCREEN_WIDTH = 208 
SCREEN_HEIGHT = 96
SpiteSheet = PIL.Image.open('SpriteSheet.png')
# Function to load Tiled map (TMX) data (tilemap layers)
def load_tiled_map(tmx_filename):
    # Parse the TMX XML file
    tree = ET.parse(tmx_filename)
    root = tree.getroot()

    # Extract map dimensions and other properties with error handling
    try:
        map_width = int(root.attrib['width'])
        map_height = int(root.attrib['height'])
    except KeyError as e:
        print(f"Error: Missing attribute {e} in the map element.")
        return None, None, None, None

    # Find tileset images and tile ids
    tilesets = {}
    for tileset in root.findall('tileset'):
        try:
            firstgid = int(tileset.attrib['firstgid'])
            image = tileset.find('image')
            if image is not None:
                tileset_image = image.attrib.get('source')
                tilesets[firstgid] = tileset_image
            else:
                print(f"Warning: No image found for tileset with firstgid {firstgid}")
        except KeyError as e:
            print(f"Error: Missing attribute {e} in the tileset element.")

    # Extract layers data (in CSV format)
    layers = []
    for layer in root.findall('layer'):
        data = layer.find('data').text.strip().split(',')
        data = [int(value) for value in data]  # Convert to integer values
        layers.append(data)

    return layers, tilesets, map_width, map_height

# Function to load tiles from a sprite sheet
def load_tiles_from_spritesheet(spritesheet_path, tile_width, tile_height):
    spritesheet = pygame.image.load(SpriteSheet).convert_alpha()
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
def draw_tilemap(screen, layers, tile_images, map_width, map_height):
    for layer in layers:
        for row_index in range(map_height):
            for col_index in range(map_width):
                tile_id = layer[row_index * map_width + col_index]
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

    # Load the Tiled map data
    tmx_filename = "tilemap.tmx"  # Replace with your TMX file path
    layers, tilesets, map_width, map_height = load_tiled_map(tmx_filename)

    # Load tiles from the sprite sheet (assuming only one tileset)
    tile_images = {}
    for firstgid, spritesheet_path in tilesets.items():
        tile_images.update(load_tiles_from_spritesheet(spritesheet_path, TILE_SIZE, TILE_SIZE))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen before drawing new frame
        screen.fill((0, 0, 0))  # Clear with black background

        # Draw the tilemap layers
        draw_tilemap(screen, layers, tile_images, map_width, map_height)

        pygame.display.flip()
        clock.tick(60)  # Cap the frame rate to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()