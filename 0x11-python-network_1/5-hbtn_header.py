#!/usr/bin/python3
"""
    Takes in a URL, sends a request to the URL
    Displays the value of the variable X-Request-Id in the response header
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    if url is None:
        exit
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
