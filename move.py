import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Move Omar One Tile at a Time')

# Define the size of each tile (32x32 pixels)
tile_size = 32
cols, rows = 20, 16  # 20 columns and 16 rows for the grid
screen_width = cols * tile_size
screen_height = rows * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the PNG image
image = pygame.image.load('omar.png')  # Replace with the correct path
image = pygame.transform.scale(image, (tile_size, tile_size))  # Resize image to fit tile size

# Define the initial position of the image in terms of tiles (in grid coordinates)
x, y = 5, 5  # Starting position in terms of tile indices (row, column)

# Set up game clock
clock = pygame.time.Clock()

# Run the game loop
while True:
    screen.fill((255, 255, 255))  # Fill screen with white color

    # Draw a simple grid (for visualization)
    for row in range(0, screen_height, tile_size):
        for col in range(0, screen_width, tile_size):
            pygame.draw.rect(screen, (200, 200, 200), (col, row, tile_size, tile_size), 1)

    # Handle events (e.g., closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for key press events (move the image one tile at a time)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # Left arrow key
                if x > 0:  # Ensure we stay within the grid bounds
                    x -= 1
            if event.key == pygame.K_RIGHT:  # Right arrow key
                if x < (screen_width // tile_size) - 1:  # Ensure we stay within the grid bounds
                    x += 1
            if event.key == pygame.K_UP:  # Up arrow key
                if y > 0:  # Ensure we stay within the grid bounds
                    y -= 1
            if event.key == pygame.K_DOWN:  # Down arrow key
                if y < (screen_height // tile_size) - 1:  # Ensure we stay within the grid bounds
                    y += 1

    # Draw the image at the new position (scaled to fit the tile size)
    screen.blit(image, (x * tile_size, y * tile_size))  # Convert tile index to pixel position

    # Update the display
    pygame.display.update()

    # Control the frame rate (60 frames per second)
    clock.tick(60)
