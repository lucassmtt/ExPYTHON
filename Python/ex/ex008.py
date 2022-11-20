def leianum(msg):
    while True:
        num = input(msg)
        if num.isalpha():
            continue
        else:
            num = int(num)
            break
    return num


def numint(msg, msg_aviso=''):
    num = input(msg)
    while not num.isdigit():
        num = input(msg_aviso)
    num = int(num)
    return num


def dashed(num):
    return print('-'*num)


lista = []
while True:
    dashed(30)
    print(' (M) = Mostrar \n (A) = Adicionar \n (D) = Deletar \n (S) = Sair')
    dashed(30)
    resp = str(input('Digite aqui: ')).lower()[0]
    if resp == 'm':
        for index, value in enumerate(lista):
            print(f'{index} == {value} ')
        if len(lista) == 0:
            print('Sua lista está vazia!')
    if resp == 's':
        break
    if resp == 'd':
        for index, value in enumerate(lista):
            print(f'{index} = {value} ')
        while True:
            apagar = leianum('Por favor digite um número: ')
            if apagar > len(lista):
                print('Digite um número válido')
            if apagar <= len(lista):
                break
        del lista[apagar]
    if resp == 'a':
        for index, value in enumerate(lista):
            print(f'{index} == {value}')
        element = str(input('O que você quer adicionar? '))
        dashed(30)
        pos = numint(msg='Digite em qual posição gostaria de adicionar: ', msg_aviso='Você digitou incorretamente, por favor digite o lugar que você quer colocar: ')
        dashed(30)
        if pos > len(lista):
            print('O valor que você digitou está acima, portando irei adicionar no final!')
        dashed(30)
        lista.insert(pos, element)
        for index, value in enumerate(lista):
            print(f'{index} == {value}')
print('FIM')