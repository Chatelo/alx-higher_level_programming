#!/usr/bin/python3

"""
Retrieves the 10 most recent commits from a repository by a given user.
The first argument is the repository name.
The second argument is the owner name. Uses the GitHub API to fetch the commits.
Prints the commits in the format "<sha>: <author name>" (one per line).
"""
import sys
import requests

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit["sha"]
        author = commit["commit"]["author"]["name"]
        print(f"{sha}: {author}")
