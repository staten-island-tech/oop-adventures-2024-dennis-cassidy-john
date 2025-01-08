from PIL import Image, ImageDraw
import os

# Load the base sprite
base_sprite_path = "omar.PNG"  # Update to your sprite file name
sprite = Image.open(base_sprite_path).convert("RGBA")

# Function to create walking frames
def create_walking_frames(sprite):
    frames = []
    width, height = sprite.size

    # Create multiple frames with slight changes
    for i in range(3):  # Number of frames
        frame = sprite.copy()
        draw = ImageDraw.Draw(frame)

        # Simulate leg movement
        if i == 0:  # First frame: move left leg forward
            draw.rectangle((20, height - 20, 24, height), fill=(0, 0, 0, 255))  # Example movement
        elif i == 1:  # Second frame: move right leg forward
            draw.rectangle((40, height - 20, 44, height), fill=(0, 0, 0, 255))
        elif i == 2:  # Third frame: neutral position
            draw.rectangle((30, height - 20, 34, height), fill=(0, 0, 0, 255))

        frames.append(frame)
    return frames

# Generate frames
walking_frames = create_walking_frames(sprite)

# Save frames to a folder
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

for idx, frame in enumerate(walking_frames, start=1):
    frame.save(f"{output_folder}/frame{idx}.png")

print(f"Frames saved to the '{output_folder}' folder.")