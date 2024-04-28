#!/usr/bin/python3
"""a script that fetches a website"""
import requests
from sys import argv


if __name__ == "__main__":

    r = requests.get(argv[1])
    res_id = r.headers.get("X-Request-Id")
    print(res_id)
