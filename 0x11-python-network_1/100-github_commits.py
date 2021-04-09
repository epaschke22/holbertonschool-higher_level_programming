#!/usr/bin/python3
"""get 10 commits from github repo"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
    r = requests.get(url, params={'per_page': 10}).json()
    for i in r:
        print("{}: {}".format(i['sha'], i['commit']['author']['name']))
