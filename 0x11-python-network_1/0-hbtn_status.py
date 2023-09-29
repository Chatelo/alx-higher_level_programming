#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    """This line degines the target url in a variable named url"""
    url = "https://alx-intranet.hbtn.io/status"

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        """This line reads the response and display the body responses in the print satements."""
        body = response.read()

        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

