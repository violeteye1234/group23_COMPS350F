# test_pillow.py
from PIL import Image

# Check if Pillow is working by opening an image file
try:
    with Image.open("example.jpg") as img:
        img.show()
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
