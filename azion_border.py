import requests
import json

# você precisa alterar essas variáveis
authorization = ''
id = ''

# daqui para baixo, não altere nada!
params = {"format": "json"}

response = requests.get('https://api.azionapi.net/network_lists/ID',
                        headers={
                            'Content-Type': 'application/json',
                            'Accept': 'application/json; version=3',
                            'Authorization': authorization,
                            'id': id
                        })
data = response.json()
ips = data['results']['items_values']

with open('terraform.tfvars.json', 'w') as f:
    json.dump({'items_values': ips}, f)
