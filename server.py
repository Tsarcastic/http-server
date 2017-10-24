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
    conn, addr = server.accept()
    buffer_length = 300
    message_complete = False
    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            break
    message = part.decode('utf8')
    conn.sendall(message.encode('utf8'))
    conn.close()
    server.close()


def response_ok():
    """Return an HTTP 200 message."""
    two_hundred = """HTTP/1.1 200 OK
                Content-Type: text/plain"""
    return two_hundred.encode('utf8')


def response_error():
    """Return an HTTP 500 message."""
    five_hundred = """HTTP/1.1 500 UH-OH<CRLF>
                    Date: Mon, 23 May 2005 22:38:34 GMT<CRLF>"""
    return five_hundred.encode('utf-8')


if __name__ == '__main__':
    server()
