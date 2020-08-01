#!/usr/bin/python3
"""
Send a file to a receiving socket
"""
import socket
import os
import tqdm


def send_file(ip_addr, port, filename):
    """
    Open socket and send file
    """
    # Define constants
    file_size = os.path.getsize(filename)
    separator = "<separator>"
    buffer_size = 4096 # send 4096 bytes each time step

    # Open socket
    sending_socket = socket.socket()
    print(f"[+] Connecting to {ip_addr}:{port}")
    sending_socket.connect((ip_addr, port))
    print("[+] Connected.")

    # Send filename and size
    sending_socket.send(f"{filename}{separator}{file_size}".encode())

    # Start sending file
    progress = tqdm.tqdm(range(file_size), f"Sending {filename}", \
            unit="B", unit_scale=True, unit_divisor=1024)

    with open(filename, "rb") as input_file:
        for _ in progress:
            # Read bytes from file
            bytes_read = input_file.read(buffer_size)
            if not bytes_read:
                # Transmitting is done
                break
            # Sendall to assure transmission
            # Might change with wired
            sending_socket.sendall(bytes_read)
            # Update progress bar
            progress.update(len(bytes_read))

    # close socket
    sending_socket.close()

#send_file("192.168.50.161", 5001, "./example_files/UMVPN-4.8.03052.tar.gz")
