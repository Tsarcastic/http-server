"""Test client's ability to send a message and receive an echo."""
import pytest


def test_send_and_receive_echo():
    """Send an echo to server and hear an echo back."""
    from client import client
    assert client('echo echo echo') == 'echo echo echo'


def test_response_ok():
    """Test if response ok returns a HTTP200 message."""
    from server import response_ok
    assert len(response_ok()) > 50


def test_response_error():
    """Test response error function."""
    from server import response_error
    assert len(response_error()) > 50
