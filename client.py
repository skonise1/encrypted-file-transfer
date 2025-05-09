import socket
from cryptography.fernet import Fernet

# Load the AES key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Read the file to send
with open("message.txt", "rb") as f:
    file_data = f.read()

# Encrypt the file data
encrypted_data = fernet.encrypt(file_data)

# Create a TCP socket and connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

# Send encrypted data
client_socket.sendall(encrypted_data)

print("📤 Encrypted file sent to server.")

# Close connection
client_socket.close()
