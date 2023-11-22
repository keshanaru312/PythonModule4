#!/usr/bin/env python3

import os
import PIL
from PIL import Image

image_dir = "./supplier-data/images"

image_count = 0

# if not os.path.exists(icons_dir):
#     os.makedirs(icons_dir)

for filename in os.listdir(image_dir):
    image_path = os.path.join(image_dir, filename)

    try:
        image = Image.open(image_path)
        # width, height = image.size
        # format = image.format

        print(f"Processing image: {filename}")
        # print(f"Format: {format}")
        # print(f"Size: {width}x{height}")
        print("-------------------------------------")
        image_count += 1

       # Convert the image mode to RGB if it's not already
        resized_image = image.convert("RGB")
        resized_image = resized_image.resize((600, 400))

        # Save the resized image as a JPEG in the icons_dir directory
        new_filename = filename.split(".")[0] + ".jpeg"
        new_image_path = os.path.join(image_dir, new_filename)

        if os.path.exists(new_image_path):
            os.remove(new_image_path)  # Delete the file if it already exists
            print(f"Removed old image at: {new_image_path}")

        resized_image.save(new_image_path)
        print(f"Saved image to: {new_image_path}")

    except PIL.UnidentifiedImageError:
        print("Error: Unable to identify image file")
        print(f"Filename: {filename}")
    except PIL.UnidentifiedImageError:
        print("Error: Unable to identify image file")
        print(f"Filename: {filename}")

print(f"Total images processed: {image_count}")
