import socket
import tqdm
import os

# Device IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001

# Receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# Create the server socket
s = socket.socket()

# Bind the socket to local address
s.bind((SERVER_HOST, SERVER_PORT))

# 5 max connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

# Accept connection if there is any 
client_socket, address = s.accept()
print(f"[+] {address} is connected.")

# Receive file
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

# Remove absolute path
filename = os.path.basename(filename)

# Convert to integer
filesize = int(filesize)

# start receiving the file from the socket
# and writing to the file stream
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    for _ in progress:
        # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            # nothing is received
            # file transmitting is done
            break
        # write to the file the bytes we just received
        f.write(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))

# close the client socket
client_socket.close()
# close the server socket
s.close()
