#!/usr/bin/python3
"""display value of the X-Id variable found in the header of the response."""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":

    with urlopen(argv[1]) as resp:
        req_id = resp.getheader("X-Request-Id")
        print(req_id)
