"""Runs multiple instances of server.py to enable asynchronous activation."""
import socket
import sys
import codecs
import os
import mimetypes
from gevent import StreamServer


our_server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)

address = ('127.0.0.1', 5003)
our_server.bind(address)
our_server.listen()


def server():
    """Server function that listens for incoming requests from client."""
    try:
        while True:
            print('Connection accepted')
            conn, addr = our_server.accept()
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
        our_server.close()
        sys.exit()


def response_ok(contents, content_type, size):
    """Return an HTTP 200 message."""
    two_hundred = 'HTTP/1.1 200 OK\r\nContent-Type: {}\r\nContent-Length: {}\r\n\r\n{}@'.format(content_type, size, contents)
    return two_hundred.encode('utf8')


def response_error(code, phrase):
    """Return an HTTP 500 message."""
    five_hundred = """HTTP/1.1 {} {}
Content-Type: text/plain

@""".format(code, phrase)
    return five_hundred.encode('utf-8')


def parse_request(request):
    """Parse HTTP request and validate carriage returns, method, HTTP version, and existence of host header."""
    the_split = request.split('\r\n')
    header = the_split[0]
    host = the_split[1]
    method, uri, http_vers = header.split(' ')
    host_title = host[:5]
    if method != 'GET':
        return response_error('405', 'METHOD NOT ALLOWED')
    if http_vers != 'HTTP/1.1':
        return response_error('505', 'HTTP VERSION NOT SUPPORTED')
    if host_title != 'Host:':
        return response_error('400', 'BAD REQUEST')
    else:
        try:
            contents, content_type, size = resolve_uri(uri)
            return response_ok(contents, content_type, size)
        except ValueError:
            response_ok('404', 'NOT FOUND')


def resolve_uri(uri):
    """Function accepts uri passed in request and return a body for a response along with an indication of the content."""
    wd = os.path.abspath(__file__).rstrip('/server.py')
    path_to_file = wd + '/webroot' + uri
    if os.path.isfile(path_to_file):
        contents = ''
        with codecs.open(path_to_file, errors='ignore') as file_output:
            contents = file_output.read()
        content_type = mimetypes.guess_type(str(path_to_file))[0]
        size = os.path.getsize(path_to_file)
        return contents, content_type, size
    else:
        contents = ''
        content_type = "directory"
        inside_dir = os.listdir(path_to_file)
        for item in inside_dir:
            contents += "<ul><li> {} </li></ul>\r\n".format(item)
        return contents, content_type, 'N/A'

gevent_server = StreamServer(our_server, server)


if __name__ == '__main__':
    print("Server is running")
    gevent_server().serve_forever()
