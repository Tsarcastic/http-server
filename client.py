#!/usr/bin/python
# -*- coding: utf8 -*-
"""Client portion of the exercise on day 6 of Python 401."""
import socket

def client():
    info = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    message = u'This is a fancy message, containing über-important information'
    client.sendall(message.encode('utf8'))


if __name__ == '__main__':
    client()
