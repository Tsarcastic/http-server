"""Test client's ability to send a message and receive an echo."""
import pytest


# def test_send_and_receive_echo():
#     """Send an echo to server and hear an echo back."""
#     from client import client
#     assert client('echo echo echo') == 'echo echo echo'


# def test_message_longer_than_buffer():
#     """Test to see if returns message."""
#     from client import client
#     assert client('this is a longggggg string') == 'this is a longggggg string'


# def test_same_as_buffer():
#     """Test to see if message sent that is same length is returned."""
#     from client import client
#     assert client('eightchr') == 'eightchr'


# def test_weird_chars():
#     """Test to see if message sent that is same length is returned."""
#     from client import client
#     assert client(u'blöd') == u'blöd'


# def test_short_buffer():
#     """Send an echo to server shorted than buffer."""
#     from client import client
#     assert client('short') == 'short'


def test_response_ok():
    """Check if correct message sent when response ok called."""
    from server import response_ok
    assert response_ok() == b"""HTTP/1.1 200 OK
Content-Type: text/plain

@"""


def test_response_error():
    """Check if correct message sent when response ok called."""
    from server import response_error
    assert response_error('405', 'METHOD NOT ALLOWED') == b"""HTTP/1.1 405 METHOD NOT ALLOWED
Content-Type: text/plain

@"""


def test_full_functionality_200():
    """Functional test from start to finish for well-formed request."""
    from client import client
    client('GET /index.html HTTP/1.1\r\nHost: www.google.com\r\n\r\n') == b"""HTTP/1.1 200 OK
Content-Type: text/plain

@"""


def test_full_functionality_405():
    """Functional test from start to finish for well-formed request."""
    from client import client
    client('PUT /index.html HTTP/1.1\r\nHost: www.google.com\r\n\r\n') == b"""HTTP/1.1 405 METHOD NOT ALLOWED
Content-Type: text/plain

@"""


def test_for_405_error():
    """Check if proper message sent if GET request not present."""
    from server import parse_request
    assert parse_request('POST /index.html HTTP/1.1\r\nHost: www.google.com\r\n\r\n') == b"""HTTP/1.1 405 METHOD NOT ALLOWED
Content-Type: text/plain

@"""


def test_for_505_error():
    """Check if proper message sent if wrong HTTP version sent."""
    from server import parse_request
    assert parse_request('GET /index.html HTTP/1.0\r\nHost: www.google.com\r\n\r\n') == b"""HTTP/1.1 505 HTTP VERSION NOT SUPPORTED
Content-Type: text/plain

@"""


def test_for_400_error():
    """Check if host head present send send proper error."""
    from server import parse_request
    assert parse_request('GET /index.html HTTP/1.1\r\nHttt: www.google.com\r\n\r\n') == b"""HTTP/1.1 400 BAD REQUEST
Content-Type: text/plain

@"""
