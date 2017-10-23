"""Client portion of the exercise on day 6 of Python 401."""
import socket


def main():
    """The main server function."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)

    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen()
    conn, addr = server.accept()

if __name__ == '__main__':
    main()