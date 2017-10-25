"""Test client's ability to send a message and receive an echo."""
import pytest


# def test_send_and_receive_echo():
#     """Send an echo to server and hear an echo back."""
#     from client import client
#     assert client('echo echo echo') == 'echo echo echo'


def test_response_ok():
    """Test if response ok returns a HTTP200 message."""
    from server import response_ok
    assert len(response_ok()) > 0


def test_response_ok_200_message():
    """Test to see if response string sent back equals expected message."""
    from server import response_ok
    expected_response = """HTTP/1.1 200 OK
Content-Type: text/plain

"""
    assert response_ok() == expected_response.encode('utf8')

def test_method_validation_returns_true:
    from server import method_validation
    new = "GET /index.html HTTP/1.1"[:3]
    assert method_validation(new) == True
def test_response_error():
    """Test response error function."""
    from server import response_error
    assert len(response_error()) > 0
