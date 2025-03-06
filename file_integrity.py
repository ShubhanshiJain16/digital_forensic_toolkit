import hashlib

def hash_file(file_path, hash_type="sha256"):
    """Compute hash of a file using specified hash algorithm."""
    try:
        hasher = hashlib.new(hash_type)
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):  # Read file in chunks
                hasher.update(chunk)
        return hasher.hexdigest()
    
    except FileNotFoundError:
        print("\n[!] Error: File not found.")
        return None
    except Exception as e:
        print(f"\n[!] Error: {e}")
        return None

if __name__ == "__main__":
    file_path = input("Enter file path: ")
    print("\n[+] Generating Hashes...")
    print(f"MD5:    {hash_file(file_path, 'md5')}")
    print(f"SHA-1:  {hash_file(file_path, 'sha1')}")
    print(f"SHA-256:{hash_file(file_path, 'sha256')}")
