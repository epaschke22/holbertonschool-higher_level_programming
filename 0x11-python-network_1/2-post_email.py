#!/usr/bin/python3
"""sends request to url with an email"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    emaildict = {'email' : argv[2]}
    email = urllib.parse.urlencode(emaildict)
    email = email.encode('ascii')
    req = urllib.request.Request(argv[1], email)
    with urllib.request.urlopen(argv[1]) as response:
        the_page = response.read()
        print(the_page)
