import os
from cryptography.fernet import Fernet

# --- 1. Key Management ---
def load_or_create_key():
    """
    Check if a key exists; if not, generate a new one and save it.
    """
    if os.path.exists("secret.key"):
        return open("secret.key", "rb").read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

# --- 2. File Encryption Function ---
def encrypt_file(file_path, key):
    """
    Encrypts a file using AES-256 (Fernet) encryption.
    """
    f = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
        
        encrypted_data = f.encrypt(file_data)
        
        output_file = file_path + ".enc"
        with open(output_file, "wb") as file:
            file.write(encrypted_data)
        print(f"[+] Success: '{file_path}' has been encrypted to '{output_file}'")
    except FileNotFoundError:
        print(f"[-] Error: The file '{file_path}' was not found.")

# --- 3. File Decryption Function ---
def decrypt_file(file_path, key):
    """
    Decrypts an encrypted file back to its original form.
    """
    f = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        
        decrypted_data = f.decrypt(encrypted_data)
        
        # Saves the restored file with a suffix
        decrypted_file_path = file_path.replace(".enc", "_restored.txt")
        with open(decrypted_file_path, "wb") as file:
            file.write(decrypted_data)
        print(f"[+] Success: File decrypted and saved as '{decrypted_file_path}'")
    except Exception as e:
        print(f"[-] Error: Decryption failed. Make sure you have the correct key.")

# --- Main Application Logic ---
def main():
    print("==================================================")
    print("   🔐 Secure Cryptography Vault v2.0 - Eng. Dalaa ")
    print("==================================================")
    
    key = load_or_create_key()
    
    print("\n[Options]")
    print("1. (E)ncrypt a file")
    print("2. (D)ecrypt a file")
    
    choice = input("\nSelect an option (E/D): ").upper()
    filename = input("Enter the target filename: ")
    
    if choice == 'E':
        encrypt_file(filename, key)
    elif choice == 'D':
        decrypt_file(filename, key)
    else:
        print("[-] Invalid choice! Please select E or D.")

if __name__ == "__main__":
    main()
