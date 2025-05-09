import socket
from cryptography.fernet import Fernet

# Load the AES key from file
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind it to localhost and port 9999
server_socket.bind(('localhost', 9999))
server_socket.listen(1)

print("🔌 Server is listening on port 9999...")

# Accept a connection from client
conn, addr = server_socket.accept()
print(f"✅ Connected by {addr}")

# Receive the encrypted data
encrypted_data = conn.recv(4096)

# Decrypt the data
decrypted_data = fernet.decrypt(encrypted_data)

# Save the original content to a file
with open("received_file.txt", "wb") as f:
    f.write(decrypted_data)

print("📥 File received and saved as 'received_file.txt'")

# Close connection
conn.close()
server_socket.close()
