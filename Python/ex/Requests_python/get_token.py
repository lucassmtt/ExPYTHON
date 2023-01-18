PATH_TOKEN = 'token.txt'

with open(PATH_TOKEN, 'r') as file:
    token = f'Bearer {file.readline()}'
    # print(token)