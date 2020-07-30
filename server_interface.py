"""
Command Line Interface for music distribution
"""

import os
import file_send

class music:
    """
    Object to maintain program
    """
    def __init__(self):
        self.ip_addr = ["192.168.50.161"]
        self.port = 5001

    def transmit_file(self):
        """
        Send file to all devices in cluster
        """
        for ip in self.ip_addr:
        file_send.send_file(ip_addr, port, filename):

            pass


def cli():
    """
    Lauch cli
    """
    print("-------------")
    print("Music Sockets")
    print("-------------")

    while True:
        # Take input from user
        command = input('$ ')

        # List options
        if command == 'help':
            print('helping')
            print('Enter albums to view all albums')
            print('Enter songs to view all songs')
            print('Enter artists to view all artists')
            print('Enter queue with file or dir name to send')

        elif command == 'exit':
            print('Shutting down...')
            exit()

        else:
            os.system(command)

cli()
