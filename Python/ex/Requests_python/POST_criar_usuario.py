import requests
from pprint import pprint

url = 'http://127.0.0.1:3001/users'

user_data = {
    "nome": "José Maria",
    "password": "1234567",
    "email": "josemaria@hotmail.com"
}

response = requests.post(url=url, json=user_data)

if 200 <= response.status_code <= 299:
    print(f'Success {response.status_code}')
    print(f'Reason {response.reason}')
    print(f'Text {response.text}')
    print(f'JSON {response.json()}')
else:
    print(f'Success {response.status_code}')
    print(f'Reason {response.reason}')
    print(f'Text {response.text}')
