#!/usr/bin/python3
"""gets the X-Request-Id value of a url"""
from urllib import request
from sys import argv


with request.urlopen(argv[1]) as response:
    html = response.info()
    print(html['X-Request-Id'])
