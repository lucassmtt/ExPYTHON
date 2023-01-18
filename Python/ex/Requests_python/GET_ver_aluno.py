import requests
from pprint import pprint
from get_token import token

url = 'http://127.0.0.1:3001/alunos/1'

# headers = {
#     'Authorization': token
# }

# aluno_data = {
# 	"nome": "Gabriel2",
# 	"sobrenome": "Firmino2",
# 	"email": "gabrielmatador_firmino2@email.com",
# 	"idade": "50",
# 	"peso": "91",
# 	"altura": "1.60"
# }

response = requests.get(url=url)

if 200 <= response.status_code <= 299:
    print(f'Success {response.status_code}')
    print(f'Reason {response.reason}')
    # print(f'Text {response.text}')
    response_data = response.json()
    print(response_data['nome'])
    print(response_data['sobrenome'])
    print(response_data['email'])

else:
    print(f'Success {response.status_code}')
    print(f'Reason {response.reason}')
    print(f'Text {response.text}')
