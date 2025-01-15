import pygame
import csv
import os
from PIL import Image, ImageDraw, ImageFont
import module

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        # Manual load in: self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class TileMap:
    def __init__(self, filename, spritesheet, tile_size=16):
        self.tile_size = tile_size
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.map_w = len(self.tiles[0]) * self.tile_size
        self.map_h = len(self.tiles) * self.tile_size
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))

    def load_tiles(self, filename):
        tile_data = self.read_csv(filename)
        tiles = []
        for row_index, row in enumerate(tile_data):
            for col_index, tile in enumerate(row):
                if tile != "-1":  # Assuming -1 means empty space
                    tiles.append(Tile(tile, col_index * self.tile_size, row_index * self.tile_size, self.spritesheet))
        return tiles

    def read_csv(self, filename):
        map_data = []
        with open(os.path.join(filename)) as data:
            reader = csv.reader(data, delimiter=",")
            for row in reader:
                map_data.append(list(row))
        return map_data

    @staticmethod
    def slice_and_label_tilemap(tilemap_path, output_path, tile_size):
        tilemap = Image.open(tilemap_path)
        tilemap_width, tilemap_height = tilemap.size

        labeled_tilemap = Image.new("RGBA", (tilemap_width, tilemap_height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(labeled_tilemap)

        try:
            font = ImageFont.truetype("arial.ttf", 14)
        except IOError:
            font = ImageFont.load_default()

        tile_id = 0
        for y in range(0, tilemap_height, tile_size):
            for x in range(0, tilemap_width, tile_size):
                tile = tilemap.crop((x, y, x + tile_size, y + tile_size))
                labeled_tilemap.paste(tile, (x, y))

                label = str(tile_id)
                text_width, text_height = draw.textsize(label, font=font)
                label_x = x + (tile_size - text_width) // 2
                label_y = y + (tile_size - text_height) // 2
                draw.text((label_x, label_y), label, fill="red", font=font)

                tile_id += 1

        labeled_tilemap.save(output_path)
        print(f"Labeled tilemap saved to {output_path}")