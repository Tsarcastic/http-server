# HTTP Server Project

## Description

The files contained in this repository create a server that can accept requests from a client, and then echos back to the client. The test_servers.py file contains test for messages shorter and longer than the buffer length, non-ASCII characters, and messages that are an exact multiple of the buffer length.

### Contributors
Matt Favoino
Brendan Davis

### Additions for Step 1

Added functionality to return a properly formatted HTTP response to the client with response_ok and response_error functions.

### Additions for Step 2

Added parse_request function to validate request from client to ensure proper formatting, GET request, HTTP version 1.1, and the existence of a host header. Depending on the error in the request, the client will receive an applicable response.

### Additons for Step 3

Added a sample webroot directory to the repository the serves files with a proper request from the client. The resolve uri function adds this functionality, and incorporates the file with a 200 response.

### Acknowledgements
https://stackoverflow.com/questions/2611205/how-do-i-write-raw-binary-data-in-python
https://www.devdungeon.com/content/working-binary-data-python
http://python-future.org/unicode_literals.html
