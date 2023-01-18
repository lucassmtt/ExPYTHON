import requests

url = 'http://localhost:3001/images/1674060656816_14279.png'
# url = 'https://images.pexels.com/photos/301599/pexels-photo-301599.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
nome_arq = url.split('/')[-1]

response = requests.get(url)

if 200 <= response.status_code <= 299:
    print(response.status_code)
    print(response.reason)

    with open(nome_arq, 'wb') as file:
        file.write(response.content)

else:
    print(response.status_code)
    print(response.reason)
    print(response.text)