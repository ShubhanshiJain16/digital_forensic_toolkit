from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if exif_data:
            print("\n[+] Metadata Extracted:")
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")
        else:
            print("\n[-] No metadata found.")

    except Exception as e:
        print(f"\n[!] Error: {e}")

# Example Usage
if __name__ == "__main__":
    image_path = input("Enter image path: ")
    extract_metadata(image_path)
