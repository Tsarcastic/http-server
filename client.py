#!/usr/bin/python
# -*- coding: utf8 -*-
"""Client portion of the exercise on day 6 of Python 401."""
import socket
import sys


def client(user_mess):
    """The main client function."""
    info = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    message = user_mess
    client.sendall(message.encode('utf8'))
    buffer_length = 300
    message_complete = False
    while not message_complete:
        part = client.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            break
    client.close()


if __name__ == '__main__':
    client(sys.argv[1])
