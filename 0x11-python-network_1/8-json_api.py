#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys
import json

if len(sys.argv) < 2:
    q = ""
else:
    q = sys.argv[1]

try:
    response = requests.post(
        'http://0.0.0.0:5000/search_user',
        data={'q': q}
    )
    data = response.json()
    if data:
        print("[{:d}] {}".format(data['id'], data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
except requests.exceptions.RequestException as e:
    print("Error:", e)
