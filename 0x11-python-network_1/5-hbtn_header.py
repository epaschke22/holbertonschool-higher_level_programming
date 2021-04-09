#!/usr/bin/python3
"""gets the X-Request-Id value of a url"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers['X-Request-Id'])
