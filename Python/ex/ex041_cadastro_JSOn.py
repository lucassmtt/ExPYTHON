import json

def is_string(msg, aviso=''):
    while True:
        string = input(msg)
        if string.isalpha():
            string = str(string)
            break
        print(aviso)
    return string

def is_number(msg, aviso=''):
    while True:
        number = input(msg)
        if number.isnumeric():
            number = int(number)
            break
        print(aviso)
    return number
def underline(n):
    return print(n* '-')


cont_id = 0
pessoas = {}
resp = 0

with open('ex041_cadastro_usando_json_identifier.json', 'r+') as arquivo:
    lendo = arquivo.readlines()
    for i in lendo:
        if i.isnumeric():
            i = int(i)
            identificador = i


while resp != 3:
    print('Digite o número para fazer alguma operação...')
    print('''
        1 == Cadastrar novas pessoas
        2 == Ver pessoas cadastradas
        3 == Sair

    ''')
    resp = is_number(': ')
    if resp == 1:
        pessoa = {}
        nome = is_string('Digite seu nome: ', aviso='Digite seu nome corretamente, por favor: ')
        idade = is_number('Digite sua idade', aviso='Digite sua idade corretamente, por favor: ')
        numero_notas = is_number('Quantas notas você teve? ')
        notas = []
        cont = 1
        for nota in range(numero_notas):

            while True:
                nota_verif = is_number(f'Digite sua nota número {cont}: ')
                if 0 <= nota_verif <= 10:
                    cont += 1
                    notas.append(nota_verif)
                    break
                else:
                    print('Por favor digite sua nota, corretamente...')

        pessoa.setdefault('nome', nome)
        pessoa.setdefault('idade', idade)
        pessoa.setdefault('notas', notas)
        pessoas.setdefault(f'pessoa_id_{identificador}', pessoa)
        pessoa = {}
        identificador += 1
    if resp == 2:
        while True:
            login = input('Digite seu login de administrador: ')
            senha = input('Digite sua senha...')
            if login == 'MOTTA' and senha == '12345678':
                with open('ex041_cadastro_usando.json', 'r') as arquivo:
                    print(json.load(arquivo))
                break

with open('ex041_cadastro_usando.json', 'a+') as arquivo:
    json.dump(pessoas, arquivo, ensure_ascii=False, indent=2)


with open('ex041_cadastro_usando_json_identifier.json', 'w') as arquivo:
    json.dump(identificador, arquivo)
print(identificador)