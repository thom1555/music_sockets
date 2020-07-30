import socket
import tqdm
import os


def send_file(ip_addr, port, filename):
    """
    Open socket and send file
    """
    # Define constants
    FILE_SIZE = os.path.getsize(filename)
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096 # send 4096 bytes each time step

    # Open socket
    s = socket.socket()
    print(f"[+] Connecting to {ip_addr}:{port}")
    s.connect((ip_addr, port))
    print("[+] Connected.")

    # Send filename and size
    s.send(f"{filename}{SEPARATOR}{FILE_SIZE}".encode())

    # Start sending file
    progress = tqdm.tqdm(range(FILE_SIZE), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

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

send_file("192.168.50.161", 5001, "./example_files/UMVPN-4.8.03052.tar.gz")

