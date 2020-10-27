import requests
import json

params = {"format": "json"}

response = requests.get(f"https://api.azionapi.net/network_lists/ID",
 headers={
           'Content-Type': 'application/json',
           'Accept': 'application/json; version=3',
           'Authorization': '',
           'id': ''
 }
)

data = response.json()
ips = data['results']['items_values']
with open('terraform.tfvars.json', 'w') as f:
    json.dump({'items_values': ips}, f)