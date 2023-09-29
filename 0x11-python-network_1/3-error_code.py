#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response(decoded in utf-8).
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    """Sends a request to the URL and display the response body."""
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            """Retrieve and display the response body."""
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        """Handle HTTP errors and print the error code."""
        print("Error code:", e.code)
