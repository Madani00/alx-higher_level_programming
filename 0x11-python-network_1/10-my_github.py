#!/usr/bin/python3
"""
a script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        username = sys.argv[1]
        token = sys.argv[2]

        url = 'https://api.github.com/user'
        response = requests.get(url, auth=(username, token))

        if response.status_code == 200:
            print(response.json()['id'])
        else:
            print(None)
