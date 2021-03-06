#!/usr/bin/python3
"""search api"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""
    arg = {'q': letter}
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=arg).json()
        if not r:
            print("No result")
        else:
            print("[{}] {}".format(r['id'], r['name']))
    except:
        print("Not a valid JSON")
