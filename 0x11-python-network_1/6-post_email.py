#!/usr/bin/python
"""sends a POST request to the passed URL with the email as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":

    em = {"email": argv[2]}
    r = requests.post(argv[1], data=em)
    print(r.text)
