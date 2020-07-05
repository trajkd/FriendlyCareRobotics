#!bin/usr/env python

import requests

url = "https://hackathon.tim.it/CRI2/status"

payload = {}
headers = {
  'apikey': 'izz6sXoXn00q6TqYt6VmtWUCqBpznsPy'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))