"""
Command Line Interface for music distribution
"""

from os import listdir, system
from os.path import isfile, join
import socket
import sys
import syslog
import send_file


def log(msg, level):
    """
    Send a message to the music.log file
    """
    if level == 'debug':
        syslog.syslog(syslog.LOG_LOCAL6 | syslog.LOG_DEBUG, msg)

    elif level == 'info':
        syslog.syslog(syslog.LOG_LOCAL6 | syslog.LOG_INFO, msg)

    elif level == 'error':
        syslog.syslog(syslog.LOG_LOCAL6 | syslog.LOG_ERR, msg)

    elif level == 'warning':
        syslog.syslog(syslog.LOG_LOCAL6 | syslog.LOG_WARNING, msg)

    else:
        print('Error with log message ', msg)
        print('Cannot syslog at that level...')


class Music:
    """
    Object to maintain program
    """
    def __init__(self):
        """
        List of ips in cluster
        Port to communicate over
        """
        self.ip_addr = ["192.168.50.66"]
        self.file_port = 5001
        self.comm_port = 6001



    def transmit_file(self, filepath):
        """
        Send file to all devices in cluster
        """
        for address in self.ip_addr:
            send_file.send_file(address, self.file_port, filepath)


    def change_port(self, port):
        """
        Send message to all client to change port to communicate over
        """
        for address in self.ip_addr:
            sending_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sending_socket.connect((address, self.comm_port))
            sending_socket.send(port)
            sending_socket.close()

        return True


    def file_loop(self):
        """
        Manage showing the user files
        Open new command line and take input
        """
        adding_files = True

        print('Enter file to send')
        print('Enter list to view all files')
        print('Press q to quit')

        while adding_files:
            # Loop to list and select files
            filename = input('% ')

            if filename == 'q':
                print('Exiting')
                adding_files = False

            elif filename == 'list':
                print('Listing files')
                files = [f for f in listdir('./example_files')\
                        if isfile(join('./example_files', f))]
                print(files)

            else:
                # Select file to send
                self.transmit_file('./example_files/message.txt')

        return True


    def cli(self):
        """
        Lauch cli
        """
        print("-------------")
        print("Music Sockets")
        print("-------------")

        log('Startup music sockets', 'debug')

        while True:
            # Take input from user
            command = input('$ ')

            # List options
            if command == 'help':
                print('Enter albums to view all albums')
                print('Enter songs to view all songs')
                print('Enter artists to view all artists')
                print('Enter queue with file or dir name to send')

            elif command == 'send file':
                self.file_loop()

            elif command == 'change port':
                self.change_port(5002)

            elif command == 'exit':
                print('Shutting down...')
                sys.exit()

            else:
                system(command)


program = Music()
program.cli()
