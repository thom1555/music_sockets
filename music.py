"""
Command Line Interface for music distribution
"""

import os


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
