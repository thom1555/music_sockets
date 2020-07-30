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

        os.system(command)
        exit()

cli()
