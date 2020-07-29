import socket
import tqdm
import os

SEPARATOR = "<SEOARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of server
host = "1.1.1.1"
port 5001

# Set file name
filename = "message.txt"
# Get file size
filesize = os.path.getsize(filename)

# Create socket
s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# Send filename and size
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# Start sending file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "rb") as f:
    for _ in progress:
        # Read bytes from file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # Transmitting is done
            break
        # Sendall to assure transmission
        # Might change with wired
        s.sendall(bytes_read)
        # Update progress bar
        progress.update(len(bytes_read))

# close socket
s.close()
