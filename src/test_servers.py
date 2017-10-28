"""Test client's ability to send a message and receive an echo."""
from __future__ import unicode_literals


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
    """Check if 405 sent if incorrect method used in request from client."""
    from client import client
    client('PUT /index.html HTTP/1.1\r\nHost: www.google.com\r\n\r\n') == b"""HTTP/1.1 405 METHOD NOT ALLOWED
Content-Type: text/plain

@"""


def test_for_405_error():
    """Check parse request function for improper method."""
    from server import parse_request
    assert parse_request('POST /index.html HTTP/1.1\r\nHost: www.google.com\r\n\r\n') == b"""HTTP/1.1 405 METHOD NOT ALLOWED
Content-Type: text/plain

@"""


def test_for_505_error():
    """Check parse request function for wrong HTTP version."""
    from server import parse_request
    assert parse_request('GET /index.html HTTP/1.0\r\nHost: www.google.com\r\n\r\n') == b"""HTTP/1.1 505 HTTP VERSION NOT SUPPORTED
Content-Type: text/plain

@"""


def test_for_400_error():
    """Check parse request function for bad host header."""
    from server import parse_request
    assert parse_request('GET /index.html HTTP/1.1\r\nHttt: www.google.com\r\n\r\n') == b"""HTTP/1.1 400 BAD REQUEST
Content-Type: text/plain

@"""
