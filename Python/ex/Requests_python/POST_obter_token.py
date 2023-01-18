import requests
from pprint import pprint

url = 'http://127.0.0.1:3001/tokens'

user_data = {
    "password": "1234567",
    "email": "josemaria@hotmail.com"
}

response = requests.post(url=url, json=user_data)

if 200 <= response.status_code <= 299:
    print(f'Success {response.status_code}')
    print(f'Reason {response.reason}')
    print(f'Text {response.text}')

    response_data = response.json()
    token = response_data['token']
    PATH_TOKEN = 'token.txt'

    with open(PATH_TOKEN, 'w') as arquivo:
        arquivo.write(token)


else:
    print(f'Success {response.status_code}')
    print(f'Reason {response.reason}')
    print(f'Text {response.text}')
