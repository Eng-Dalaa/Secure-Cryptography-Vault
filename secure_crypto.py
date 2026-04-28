from cryptography.fernet import Fernet

class EngDalaaVault:
    def __init__(self):
        # Generate a unique encryption key
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        # Convert text to bytes then encrypt
        return self.cipher.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        # Decrypt and return to readable text
        return self.cipher.decrypt(encrypted_data).decode()

# --- Testing the Tool ---
vault = EngDalaaVault()

print("--- 🔐 Secure Cryptography Tool by Eng. Dalaa ---")
user_input = input("Enter the sensitive data to encrypt: ")

# Encryption Process
encrypted_result = vault.encrypt_data(user_input)
print(f"\n[+] Encrypted (Ciphertext): {encrypted_result}")

# Decryption Process
decrypted_result = vault.decrypt_data(encrypted_result)
print(f"[+] Decrypted (Plaintext): {decrypted_result}")

print(f"\n[!] Secret Key: {vault.key.decode()}")
