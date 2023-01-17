import requests

#http:// -> 80
#https:// -> 443

url = 'http://localhost:3333/'
# url = 'https://freitasadvocacia.org/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.json())
print(response.text)