lista = [
    {'nome': 'Luiz gustavo', 'sobrenoe': 'Lunes'},
    {'nome': 'Alexandre', 'sobrenoe': 'Armando'},
    {'nome': 'Lucas', 'sobrenoe': 'Motta'}
]

def ordena(item):
    return item['sobrenoe']
lista.sort(key=ordena)
for item in lista:
    print(item)


##OUUU
print('-'*20)
print('Versão reduzida')


lista_lambda = [
    {'nome': 'Jorge', 'Sobrenome': 'Bgmes'},
    {'nome': 'Guilherme', 'Sobrenome': 'Alves'}
]

lista_lambda.sort(key=lambda item: item['nome'])
for item in lista_lambda:
    print(item)