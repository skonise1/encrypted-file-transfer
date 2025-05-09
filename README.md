# Encrypted File Transfer using Python

This is a secure file transfer system where a client encrypts a file using AES (Fernet) and sends it to a server over TCP sockets. The server decrypts the received file and saves it.

## How It Works

- A shared encryption key is generated and saved as `secret.key`
- The client reads a file (`message.txt`), encrypts it with the key, and sends it over a socket
- The server listens for incoming files, decrypts the received data using the same key, and saves it as `received_file.txt`

## Files

- `generate_key.py`: Generates the shared encryption key (`secret.key`)
- `client.py`: Encrypts and sends the file to the server
- `server.py`: Receives and decrypts the file
- `message.txt`: Sample file to send
- `received_file.txt`: Decrypted file received by server
- `secret.key`: Shared encryption key (used by both client and server)

## How to Run the Project

- Install the required library: `pip install cryptography`  
- Generate the encryption key: `python generate_key.py`  
- Start the server in one terminal: `python server.py`  
- Run the client in another terminal: `python client.py`  

After running the above steps, the server will save the decrypted file as `received_file.txt`.

---

## Notes

- This version supports simple, small file transfers
- Never upload `secret.key` to GitHub in real-world projects — use `.gitignore`

