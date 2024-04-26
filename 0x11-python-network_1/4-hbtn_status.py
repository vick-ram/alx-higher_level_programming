#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
with only 'requests'
"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
