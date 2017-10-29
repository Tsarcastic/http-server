"""Test client's ability to send a message and receive an echo."""
from __future__ import unicode_literals
import pytest

# def test_if_uri_with_dir_sends_list():
#     """Check if a list of files is returned if the uri sent in a request is a directory."""
#     from client import client
#     assert client('GET /webroot HTTP/1.1\r\nHost: www.google.com\r\n\r\n') == b"""HTTP/1.1 200 OK\r\nContent-Type: directory\r\nContent-Length: N/A\r\n\r\n<ul><li> a_web_page.html </li></ul>\r\n\r\n<ul><li> images </li></ul>\r\n\r\n<ul><li> make_time.py </li></ul>\r\n\r\n<ul><li> sample.txt </li></ul


def test_resolve_uri_txt_type():
    """Check uri type for sample.txt file."""
    from server import resolve_uri
    contents, content_type, size = resolve_uri('/sample.txt')
    assert content_type == 'text/plain'


def test_resolve_uri_py_type():
    """Check uri type for .py file."""
    from server import resolve_uri
    contents, content_type, size = resolve_uri('/make_time.py')
    assert content_type == 'text/x-python'


def test_resolve_uri_html_type():
    """Check uri type for html file."""
    from server import resolve_uri
    contents, content_type, size = resolve_uri('/a_web_page.html')
    assert content_type == 'text/html'


def test_resolve_uri_img_type():
    """Check uri type for images directory."""
    from server import resolve_uri
    contents, content_type, size = resolve_uri('/webroot/images')
    assert content_type == 'directory'


def test_response_ok():
    """Test for functionality of response_ok."""
    from server import response_ok
    assert response_ok('contents', 'content_type', 'size').endswith(b'@')


def test_response_error():
    """Check if correct message sent when response ok called."""
    from server import response_error
    assert response_error('405', 'METHOD NOT ALLOWED') == b"""HTTP/1.1 405 METHOD NOT ALLOWED
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
