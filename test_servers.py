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
    assert response_error() == b"""HTTP/1.1 500 INTERNAL SERVER ERROR
Content-Type: text/plain

@"""


def test_full_functionality():
    """Functional test from start to finish."""
    from client import client
    client('This is a request from the client') == b"""HTTP/1.1 200 OK
Content-Type: text/plain

@"""
