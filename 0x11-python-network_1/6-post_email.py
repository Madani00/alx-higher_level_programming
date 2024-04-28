#!/usr/bin/python3
"""send a POST request to the URL with the email as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    em = {"email": argv[2]}

    r = requests.post(url, data=em)
    print(r.text)
