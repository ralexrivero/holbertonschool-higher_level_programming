#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""

from urllib import request
from sys import argv

url = argv[1]

if __name__ == "__main__":
    with request.urlopen(url) as response:
        header = response.getheader("X-Request-Id")
print(header)
