import pygame
import os

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running Animation")

# Load animation frames
def load_frames():
    frames = []
    for i in range(1, 5):  # Assuming 4 frames
        frame_path = os.path.join("frames", f"frame{i}.png")
        print(f"Loading frame: {frame_path}")  # Debug print
        frames.append(pygame.image.load(frame_path))
    return frames

# Animation setup
frames = load_frames()
current_frame = 0
frame_rate = 0.1  # Adjust to control animation speed
clock = pygame.time.Clock()

# Character position
x, y = 100, 400

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update frame
    current_frame += frame_rate
    if current_frame >= len(frames):
        current_frame = 0

    # Draw character
    screen.fill((255, 255, 255))  # Clear screen with white background
    screen.blit(frames[int(current_frame)], (x, y))
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

pygame.quit()