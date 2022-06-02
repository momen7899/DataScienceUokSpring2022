import requests
import json
from types import SimpleNamespace


data = requests.get('https://fapi.coinglass.com/api/exchange/chain/balance/list').text

obj = json.loads(data)

print(obj)