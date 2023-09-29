#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given email.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    # Get the URL and email address from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create the payload with the email parameter
    payload = {'email': email}

    # Send a POST request to the URL with the payload
    response = requests.post(url, data=payload)

    # Print the response body
    print(response.text)
