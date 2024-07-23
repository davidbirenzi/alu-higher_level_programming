#!/usr/bin/python3
"""I document you"""

import urllib.request

url = 'https://alu-intranet.hbtn.io/status'
headers = {'User-Agent': 'Mozilla/5.0'}

request = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(request) as response:
    body = response.read()

print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {body.decode('utf-8')}")
