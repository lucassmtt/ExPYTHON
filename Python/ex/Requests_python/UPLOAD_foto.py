import requests
from pprint import pprint
from get_token import token
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes

PATH_PIC = '1.png'
mimetypes = MimeTypes()
mimetypes_arq = mimetypes.guess_type(PATH_PIC)[0]
print(mimetypes_arq)

multipart = MultipartEncoder(fields={
    'aluno_id': '1',
    'foto':(PATH_PIC, open(PATH_PIC, 'rb'), mimetypes_arq)
})

url = 'http://127.0.0.1:3001/fotos'

headers = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

response = requests.post(url=url, headers=headers, data=multipart)

if 200 <= response.status_code <= 299:
    print(f'Success {response.status_code}')
    print(f'Reason {response.reason}')
    print(f'Text {response.text}')

    # response_data = response.json()
    # print(response_data)
    # token = response_data['token']
    # PATH_TOKEN = 'token.txt'

else:
    print(f'Error {response.status_code}')
    print(f'Reason {response.reason}')
    print(f'Text {response.text}')
