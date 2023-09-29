#!/usr/bin/python3
"""
Uses the GitHub API to display your user ID.

Authentication is done using Basic Authentication with a personal access...
 token as the password.
The first argument is the GitHub username.
The second argument is the personal access token.
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    data = response.json()

    if response.status_code == 200:
        print(data["id"])
    else:
        print(None)
