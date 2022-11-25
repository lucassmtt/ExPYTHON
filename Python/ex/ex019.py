'''lista = []
for numero in range(10):
    lista.append(numero)
print(lista)


#ouuu

lista_1 = [numero for numero in range(10)]
print(lista_1)

lista_2 = [
    numero * 3
    for numero in range(10)
]

print(lista_2)
'''
produtos = [
    {'dicionario': 'p1', 'preco': 20},
    {'dicionario': 'p2', 'preco': 30},
    {'dicionario': 'p3', 'preco': 40},
    ]

novos_produtos = [
    {** produto, 'preco': produto['preco'] * 2} ##Como eu quero fazer um novo dicionario com produtos, tenho que empacotar cada laço dentro de um novo dicionário
    for produto in produtos                     ##depois pegar a chave, trazer uma nova atribuição com o novo valor, no caso, X2
]


novos_produtos_com_novo_nome = [
    {** produto, 'dicionario': produto['dicionario']}
    for produto in produtos
]


print(*novos_produtos, sep='\n')
print('-'*30)
print('-'*30)
print(*novos_produtos_com_novo_nome, sep='\n')


novos_produtos_caso_o_preco_for_maior = [
    {** produto, 'preco': produto['preco'] * 1.5}
    if produto['preco'] > 25 else {**produto}
    for produto in produtos
]
print('-'*30)
print('-'*30)
print(*novos_produtos_caso_o_preco_for_maior, sep='\n')