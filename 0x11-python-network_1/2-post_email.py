#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter and displays...
 the response body.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    """Send a POST request to the URL with the email as a parameter...
      and display the response body."""
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")

    with urllib.request.urlopen(req) as response:
        """Retrieve and display the response body."""
        body = response.read().decode("utf-8")
        print(body)
