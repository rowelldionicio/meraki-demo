import requests
import json

url = "https://dashboard.meraki.com/api/v0/organizations"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
} # Demo API key from Meraki

response = requests.request("GET", url, headers=headers, data = payload)

r = json.loads(response.text)
print(r)
