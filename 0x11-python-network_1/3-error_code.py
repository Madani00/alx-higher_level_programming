#!/usr/bin/python3
"""manage urllib.error.HTTPError exceptions and print: Error code:"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            da = response.read()
            print(da.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
