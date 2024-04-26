#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id
"""
import requests
import sys

if len(sys.argv) < 3:
    print("Usage: ./10-my_github.py <username> <password>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]

try:
    response = requests.get(
        'https://api.github.com/user',
        auth=(username, password)
    )
    data = response.json()
    print(data.get('id', None))
except requests.exceptions.RequestException as e:
    print(None)
