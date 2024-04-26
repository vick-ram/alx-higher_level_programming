#!/usr/bin/python3
"""cript that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response
"""
import urllib.request
import sys

if len(sys.argv) < 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.info().get('X-Request-Id'))

