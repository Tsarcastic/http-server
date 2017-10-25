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
        incoming = part.decode('utf8')
        if len(part) < buffer_length:
            break
    write_to_stndout(incoming)
    conn.sendall(response_ok())
    conn.close()
    server.close()


def response_ok():
    """Return an HTTP 200 message."""
    two_hundred = """HTTP/1.1 200 OK
Content-Type: text/plain

"""
    return two_hundred.encode('utf8')


def response_error():
    """Return an HTTP 500 message."""
    five_hundred = """HTTP/1.1 500 UH-OH
Content-Type: text/plain

"""
    return five_hundred.encode('utf-8')


def write_to_stndout(incoming_text):
    """Write message received to txt file."""
    with open('stndout.txt', 'a') as myfile:
        myfile.write(incoming_text + '\n')


def parse_request(request):
    """Parse http request and validate all pieces."""
    the_split = request.split("\r\n")
    try:
        method_validation(the_split[0])
    except:
        raise Exception("Not a GET request")
    try:
        http_version(the_split[0])
    except:
        raise Exception("Wrong HTTP version")
    try:
        valid_host(the_split[1])
    except:
        raise Exception("Invalid host")
    return the_split[0][4:-9]


def method_validation(item):
    """Validate the item is a GET request."""
    method = item[:3]
    if method == "GET":
        return True
    else:
        return False


def http_version(item):
    """Validate the HTTP version is correct."""
    http = item[-8:]
    if http == "HTTP/1.1":
        return True
    else:
        return False


def valid_host(item):
    """Validate host header."""
    host = item[:4]
    if host == "Host":
        return True
    else:
        return False

if __name__ == '__main__':
    try:
        server()
    except KeyboardInterrupt:
        print('You pressed ctrl + c')
        pass
