"""установить библиотеку requests, выполнить get запрос, напечатать статус код и json
 структуру из response в swagger petstore, ручки: a. GET/pet/findByStatus, значение для параметра status='available' b.
  GET/user/username, значение для параметра username='string'"""

import requests
from pprint import pprint

url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available'
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)
print(response.status_code)
pprint(response.json())


url = 'https://petstore.swagger.io/v2/user/string'
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)
print(response.status_code)
pprint(response.json())
