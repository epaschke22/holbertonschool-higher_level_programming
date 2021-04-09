#!/usr/bin/python3
"""handle error codes"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
