#!/usr/bin/python3
"""takes in a letter and sends a POST request to
URL with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(argv) < 2:
        em = {"q": ""}
    else:
        em = {"q": argv[1]}

    r = requests.post(url, data=em)
    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json["id"], json["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
