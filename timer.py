import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
tile_size = 32  # Size of each tile (32x32 pixels)
cols, rows = 20, 16  # 20 columns and 16 rows for the grid
screen_width = cols * tile_size
screen_height = rows * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Move Omar One Tile at a Time on 20x16 Grid with Countdown Timer')

# Load the PNG image (Omar) and resize it to the tile size
image = pygame.image.load('omar.png')  # Replace with the correct path to your image
image = pygame.transform.scale(image, (tile_size, tile_size))  # Resize image to fit the tile size

# Define the initial position of the image in terms of tiles (grid coordinates)
x, y = 5, 5  # Starting position in terms of tile indices (row, column)

# Set up font for timer and game over text
font = pygame.font.Font(None, 36)  # Use the default font with size 36
game_over_font = pygame.font.Font(None, 72)  # Larger font for "Game Over" message

# Set up game clock
clock = pygame.time.Clock()

# Countdown time (in seconds)
countdown_time = 30  # Start the countdown at 60 seconds
start_ticks = pygame.time.get_ticks()  # Get the starting time (in milliseconds)

# Variable to track if the game is over
game_over = False

# Run the game loop
while True:
    # If game over, stop movement and show the game over message
    if game_over:
        screen.fill((255, 255, 255))  # Fill screen with white color
        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))  # Red text
        screen.blit(game_over_text, (screen_width // 4, screen_height // 3))  # Position at center
        pygame.display.update()
        continue  # Skip the rest of the game loop until the user closes the window

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
        if not game_over:  # Prevent movement when game is over
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Left arrow key
                    if x > 0:  # Ensure we stay within the grid bounds
                        x -= 1
                if event.key == pygame.K_RIGHT:  # Right arrow key
                    if x < cols - 1:  # Ensure we stay within the grid bounds
                        x += 1
                if event.key == pygame.K_UP:  # Up arrow key
                    if y > 0:  # Ensure we stay within the grid bounds
                        y -= 1
                if event.key == pygame.K_DOWN:  # Down arrow key
                    if y < rows - 1:  # Ensure we stay within the grid bounds
                        y += 1

    # Calculate the elapsed time since the start
    elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000  # Time in seconds

    # Calculate the remaining countdown time
    remaining_time = countdown_time - elapsed_time

    # If the countdown reaches zero, stop the game and set game_over to True
    if remaining_time <= 0:
        remaining_time = 0
        game_over = True  # Set the game over flag to True

    # Render the countdown timer text
    timer_text = font.render(f"Time: {remaining_time}s", True, (0, 0, 0))  # Black text
    screen.blit(timer_text, (10, 10))  # Position it at the top-left corner

    # Draw the image at the new position (scaled to fit the tile size)
    screen.blit(image, (x * tile_size, y * tile_size))  # Convert tile index to pixel position

    # Update the display
    pygame.display.update()

    # Control the frame rate (60 frames per second)
    clock.tick(30)
