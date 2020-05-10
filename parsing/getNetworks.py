import requests
import json

url = "https://dashboard.meraki.com/api/v0/organizations/537758/networks"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
}

response = requests.request("GET", url, headers=headers, data = payload)

networks = json.loads(response.text)

for n in networks:
    print('Network ID:', n['id'],'\t Name:', n['name'])
