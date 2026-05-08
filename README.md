# 🔐 Secure Cryptography Vault v2.0

A Python-based tool developed for file encryption and decryption using the *AES-256 (Fernet)* standard. This project was recently upgraded to support full file security following the *Securing Data* concepts from Harvard's CS50.

## 🚀 Features
- *File Encryption:* Secure any .txt or document file by converting it into a .enc file.
- *File Decryption:* Restore your original files using a unique secret key.
- *Key Management:* Automatically generates and manages a secret.key file for symmetric encryption.
- *CLI Interface:* User-friendly command-line interface developed and tested on *Kali Linux*.

## 🛠️ How it Works
1. The script generates a symmetric key using the cryptography library.
2. When encrypting, the file's binary data is processed and saved in an encrypted format.
3. To decrypt, the tool reads the .enc file and uses the same secret.key to restore the original content.

## 📝 Background
This tool was created as part of my cybersecurity learning journey at *KL University*. Version 2.0 specifically focuses on implementing secure data practices and handling file-system operations in Python.

---
Developed by Eng. Dalaa 🕵️‍♀️💻
