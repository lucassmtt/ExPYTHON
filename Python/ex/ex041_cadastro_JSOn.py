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


pessoa = {}
pessoas = {

}
# pessoa = {
#     'Nome': '',
#     'Idade': '',
#     'Notas': [
#
#     ]
# }
id = 0
while True:
    nome = is_string('Digite seu nome: ', aviso='Digite seu nome corretamente, por favor: ')
    idade = is_number('Digite sua idade', aviso='Digite sua idade corretamente, por favor: ')
    numero_notas = is_number('Quantas notas você teve? ')
    notas = []
    print(type(numero_notas))
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
    while True:
        print('1 == SAIR')
        underline(20)
        print('2 == CADASTRAR MAIS PESSOAS')
        underline(20)
        print('3 == VER PESSOAS CADASTRADAS(ADMIN)')
        underline(20)
        resp = is_number('Qual operação você gostaria de fazer? ')
        if resp == 1:
            break
        if resp == 2:
            continue
        if resp == 3:
            while True:
                login = input('Digite seu login de administrador: ')
                senha = input('Digite sua senha...')
                if login == 'MOTTA' and senha == '12345678':
                    print(pessoas)
                    break
    if resp == 1:
        break
