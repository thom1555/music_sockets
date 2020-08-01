#!/usr/bin/python3
"""
Daemon to run on client devices
Recieve both messages and files
"""

import recv_file


class Client:
    """
    Class to manage function of client daemon
    """
    def __init__(self, ip_addr, file_port, comm_port):
        """
        Set ip and port of server
        """
        self.ip_addr = ip_addr
        self.file_port = file_port
        self.comm_port = comm_port


    def listen_file(self):
        """
        Listen on the file sharing socket
        """
        recv_file.listen(self.ip_addr, self.file_port)

        return True


    def main_loop(self):
        """
        Listen on command and filesharing ports
        """
        pass

program = Client("192.168.50.66", 5001, 6001)
