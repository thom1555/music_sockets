#!/usr/bin/python3
"""
Listen on specified port and recieve files
"""

import socket
import os
import tqdm


def listen(server_host, server_port):
    """
    Listen on specified port for incomming files
    """
    # Receive 4096 bytes each time
    buffer_size = 4096
    separator = "<separator>"

    # Create the server socket
    recv_socket = socket.socket()

    # Bind the socket to local address
    recv_socket.bind((server_host, server_port))

    # 5 max connections
    recv_socket.listen(5)
    print(f"[*] Listening as {server_host}:{server_port}")

    # Accept connection if there is any
    client_socket, address = recv_socket.accept()
    print(f"[+] {address} is connected.")

    # Receive file
    received = client_socket.recv(buffer_size).decode()
    filename, filesize = received.split(separator)

    # Remove absolute path
    filename = os.path.basename(filename)

    # Convert to integer
    filesize = int(filesize)

    # start receiving the file from the socket
    # and writing to the file stream
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}",\
            unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as recv_file:
        for _ in progress:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(buffer_size)
            if not bytes_read:
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            recv_file.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # close the client socket
    client_socket.close()
    # close the server socket
    recv_socket.close()


server_host = "0.0.0.0"
server_port = 5001
listen(server_host, server_port)
