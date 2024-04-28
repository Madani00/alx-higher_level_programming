#!/usr/bin/python3
"""Display the value of X-Request-Id."""
import requests
from sys import argv


if __name__ == "__main__":

    r = requests.get(argv[1])
    if (r.code_status >= 400):
        print(r.code_status)
    else:
        print(r.text)
