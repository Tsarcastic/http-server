"""Test client's ability to send a message and receive an echo"""
import pytest


def test_send_and_receive_echo():
    """Send an echo to server and hear an echo back."""
    from client import client
    assert client('echo echo echo') == 'echo echo echo'
