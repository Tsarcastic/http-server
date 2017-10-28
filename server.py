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

    address = ('127.0.0.1', 5001)
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
                    message_complete = True
            incoming_mess.replace('@', '')
            outgoing_mess = parse_request(incoming_mess)
            conn.sendall(outgoing_mess)
            conn.close()
    except KeyboardInterrupt:
        print('You pressed ctrl + c')
        server.close()
        sys.exit()


def response_ok():
    """Return an HTTP 200 message."""
    two_hundred = """HTTP/1.1 200 OK
Content-Type: text/plain

@"""
    return two_hundred.encode('utf8')


def response_error(code, phrase):
    """Return an HTTP 500 message."""
    five_hundred = """HTTP/1.1 {} {}
Content-Type: text/plain

@""".format(code, phrase)
    return five_hundred.encode('utf-8')


def parse_request(request):
    """Parse http request and validate all pieces."""
    the_split = request.split('\r\n')
    # message = (the_split[0][3:-8]) + '@'
    method = the_split[0][0:3]
    http_vers = the_split[0][-8:]
    host_head = the_split[1][:5]
    if method != 'GET':
        return response_error('405', 'METHOD NOT ALLOWED')
    if http_vers != 'HTTP/1.1':
        return response_error('505', 'HTTP VERSION NOT SUPPORTED')
    if host_head != 'Host:':
        return response_error('400', 'BAD REQUEST')
    return response_ok()


if __name__ == '__main__':
    server()
