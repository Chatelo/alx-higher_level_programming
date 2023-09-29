#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id...
 header variable
"""

import urllib.request
import sys

if __name__ == "__main__":
    """Send request to the URL and display the value of X-Request-Id."""
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        """Retrieve and display the value of X-Request-Id."""
        header = response.getheader('X-Request-Id')
        print(header)
