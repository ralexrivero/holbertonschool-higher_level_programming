#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""

import urllib.request
from sys import argv

url = argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        html = response.read()
print(html)
