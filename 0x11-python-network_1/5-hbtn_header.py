#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the variable...
 X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    """Send a GET request to the URL and display the value of X-Request-Id"""
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    print(request_id)
