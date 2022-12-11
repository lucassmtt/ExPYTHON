import functools

produtos = [
    {'nome': 'Produto1', 'preco': 10},
    {'nome': 'Produto2', 'preco': 30},
    {'nome': 'Produto3', 'preco': 55},
    {'nome': 'Produto4', 'preco': 100},
]

def print_listas(lista):
    print(list(lista))


def regulation_value(produtos, porcentagem):
    return round(produtos * porcentagem)


novos_produtos = [
    {**produto, 'preco': regulation_value(produto['preco'], 3)}
    for produto in produtos
]

#print(list(novos_produtos))


novos_produtos_com_dez_por_cento_de_desconto = [
    {**produto, 'preco': regulation_value(produto['preco'], 0.9)}
    for produto in produtos
]

print_listas(novos_produtos_com_dez_por_cento_de_desconto)

