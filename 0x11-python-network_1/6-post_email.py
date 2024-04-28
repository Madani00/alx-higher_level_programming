#!/usr/bin/python
"""sends a POST request to the passed URL with the email as a parameter"""
import requests


if __name__ == "__main__":

    email = {"email": argv[2]}
    r = requests.post(argv[1], data=email)
    print(r.text)
