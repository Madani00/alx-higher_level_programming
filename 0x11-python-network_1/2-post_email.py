#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
from urllib.request import urlopen
from sys import argv
from urllib.parse import urlencode


if __name__ == "__main__":

    data = urlencode({"email": argv[2]})
    data = data.encode("ascii")

    with urlopen(argv[1], data) as resp:
        print(resp.read().decode("utf-8"))
