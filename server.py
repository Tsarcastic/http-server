#!/usr/bin/python
# -*- coding: utf8 -*-
"""Server portion of the exercise on day 6 of Python 401."""
import socket
import sys


def server():
    """The main server function."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)

    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen()
    try:
        while True:
            print('Server running')
            conn, addr = server.accept()
            buffer_length = 8
            message_complete = False
            incoming_mess = ''
            while not message_complete:
                part = conn.recv(buffer_length)
                incoming_mess += part.decode('utf8')
                if '@' in incoming_mess:
                    conn.sendall(incoming_mess.encode('utf8'))
                    conn.close()
                    message_complete = True
    except KeyboardInterrupt:
        print('You pressed ctrl + c')
        server.close()
        sys.exit()


if __name__ == '__main__':
    server()
