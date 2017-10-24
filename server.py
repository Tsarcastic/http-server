#!/usr/bin/python
# -*- coding: utf8 -*-
"""Server portion of the exercise on day 6 of Python 401."""
import socket


def server():
    """The main server function."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)

    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen()
    print("The server is now listening")
    conn, addr = server.accept()
    message = receive_message(conn)
    conn.sendall(message.encode('utf8'))
    conn.close()
    server.close()


def receive_message(conn):
    """Receives and decodes the message"""
    buffer_length = 300
    message_complete = False
    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            break
    return part.decode('utf8')


if __name__ == '__main__':
    server()
