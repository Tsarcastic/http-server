# HTTP Server Project

## Description

The files contained in this repository create a server that can accept requests from a client, and then echos back to the client. The test_servers.py file contains test for messages shorter and longer than the buffer length, non-ASCII characters, and messages that are an exact multiple of the buffer length.

### Additions for Step 1

Added functionality to return a properly formatted HTTP response to the client with response_ok and response_error functions.