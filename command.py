import http.client
import mimetypes
conn = http.client.HTTPSConnection("https://hackathon.tim.it")
payload = "{\n    \"command\": {\n        \"code\": 0,\n        \"parameters\": {\n            \"velocity\": {\n                \"linear\": 0.5,\n                \"angular\": 0.5,\n                \"duration\": 1.0\n            }\n        }\n    }\n}"
headers = {
  'apikey': 'izz6sXoXn00q6TqYt6VmtWUCqBpznsPy',
  'Content-Type': 'application/json'
}
conn.request("POST", "/CRI2/command", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
