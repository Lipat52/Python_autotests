import pytest
import json
import requests

base_url = 'https://petstore.swagger.io/v2/'
params = {'status': 'available'}
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
res = requests.get(base_url + 'pet/findByStatus', params=params, headers=headers)
print('Результат get-запроса: ', res.text)


data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res = requests.post(base_url + 'pet', headers=headers, data=json.dumps(data, ensure_ascii=False))
print('Результат post-запроса: ', res.text)


data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "barsik",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res = requests.put(base_url + 'pet', headers=headers, data=json.dumps(data, ensure_ascii=False))
pet_id = res.json().get('id')
print('Результат put-запроса: ', res.text)


res = requests.delete(base_url + f'pet/{pet_id}', headers=headers, data={'petId': pet_id})
print('Результат delete-запроса: ', res.text)
