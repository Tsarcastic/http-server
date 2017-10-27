#!/usr/bin/python
# -*- coding: utf8 -*-
"""Client portion of the exercise on day 6 of Python 401."""
import socket
import sys


def client(user_mess):
    """The main client function to send message to server."""
    user_mess += '@'
    info = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    message = user_mess
    client.sendall(message.encode('utf8'))
    buffer_length = 8
    message_complete = False
    return_message = ''
    while not message_complete:
        part = client.recv(buffer_length)
        return_message += part.decode('utf8')
        if '@' in return_message:
            stripped_reponse = return_message.replace('@', '')
            message_complete = True
    print(stripped_reponse)
    client.close()
    return stripped_reponse


if __name__ == '__main__':
    client(sys.argv[1])
