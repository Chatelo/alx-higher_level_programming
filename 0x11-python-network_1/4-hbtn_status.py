#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status and displays the ...
body of the response.
"""

import requests

if __name__ == "__main__":
    """Send a GET request to the URL and display the response body."""
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
