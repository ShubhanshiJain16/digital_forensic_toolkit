import os
from metadata_extractor import extract_metadata
from steganography_checker import check_steganography
from file_integrity import hash_file

def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    while True:
        clear_screen()
        print("\n🔍 Digital Forensics Toolkit 🔍")
        print("=" * 40)
        print("1️⃣  Extract Metadata from Image")
        print("2️⃣  Check for Hidden Data (Steganography)")
        print("3️⃣  Verify File Integrity (Hash Check)")
        print("4️⃣  Exit")
        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            image_path = input("\nEnter image path: ")
            extract_metadata(image_path)

        elif choice == "2":
            image_path = input("\nEnter image path: ")
            check_steganography(image_path)

        elif choice == "3":
            file_path = input("\nEnter file path: ")
            print("\n[+] Generating Hashes...")
            print(f"MD5:    {hash_file(file_path, 'md5')}")
            print(f"SHA-1:  {hash_file(file_path, 'sha1')}")
            print(f"SHA-256:{hash_file(file_path, 'sha256')}")

        elif choice == "4":
            print("\n[+] Exiting...")
            break

        else:
            print("\n[!] Invalid choice. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
