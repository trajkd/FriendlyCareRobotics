#!bin/usr/env python

import requests

url = "https://hackathon.tim.it/CRI2/status"

payload = {}
headers = {
  # Replace with your API key
  'apikey': 'xyladasjdj23knw22oo2no2'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))