import os
import numpy as np
from PIL import Image

def check_steganography(image_path):
    try:
        # Get file size
        file_size = os.path.getsize(image_path)
        print(f"\n[+] File Size: {file_size} bytes")

        # Open image and convert to numpy array
        image = Image.open(image_path)
        image_data = np.array(image)

        # Analyze LSB (Least Significant Bit)
        lsb_array = image_data & 1  # Extract the least significant bits
        lsb_ratio = np.mean(lsb_array)

        print(f"[+] LSB Modification Ratio: {lsb_ratio:.5f}")

        # If LSB ratio is too high, it indicates possible hidden data
        if lsb_ratio > 0.05:
            print("\n[!] Warning: Possible Steganography Detected!")
        else:
            print("\n[-] No hidden data detected.")

    except Exception as e:
        print(f"\n[!] Error: {e}")

# Example Usage
if __name__ == "__main__":
    image_path = input("Enter image path: ")
    check_steganography(image_path)
