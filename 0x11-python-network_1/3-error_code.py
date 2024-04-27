#!/usr/bin/python3
"""manage urllib.error.HTTPError exceptions and print: Error code:"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as resp:
            d = resp.read()
            print(d.decode("utf-8")
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
