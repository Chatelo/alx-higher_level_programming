#!/usr/bin/python3
"""
Sends a request to a given URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints:
Error code: followed by the value of the HTTP status code.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check the HTTP status code
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
