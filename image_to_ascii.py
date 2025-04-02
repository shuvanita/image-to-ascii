from PIL import Image
import argparse
import numpy as np

def load_image(image_path):
    """Load and convert image to grayscale"""
    try:
        image = Image.open(image_path).convert('L')  # 'L' mode converts to grayscale
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def resize_image(image, new_width=100):
    """Resize image while maintaining aspect ratio"""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def pixel_to_ascii(image, ascii_chars):
    """Convert pixels to ASCII characters"""
    pixels = np.array(image)
    ascii_str = ""
    for row in pixels:
        for pixel in row:
            # Map pixel value (0-255) to index in ascii_chars
            index = pixel * (len(ascii_chars) - 1) // 255
            ascii_str += ascii_chars[index]
        ascii_str += "\n"  # New line at end of row
    return ascii_str

def main():
    # ASCII characters from darkest to lightest
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert images to ASCII art")
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument("--width", type=int, default=100, help="Width of ASCII output")
    parser.add_argument("--output", help="Output file name")
    args = parser.parse_args()
    
    # Load and process image
    image = load_image(args.image_path)
    if not image:
        return
    
    image = resize_image(image, args.width)
    ascii_str = pixel_to_ascii(image, ASCII_CHARS)
    
    # Output result
    if args.output:
        with open(args.output, 'w') as f:
            f.write(ascii_str)
        print(f"ASCII art saved to {args.output}")
    else:
        print(ascii_str)

if __name__ == "__main__":
    main()