from functools import partial

def print_list(list_value):
    return print(list(list_value))
produtos = [
    {'nome': 'Produto1', 'preco': 10},
    {'nome': 'Produto2', 'preco': 30},
    {'nome': 'Produto3', 'preco': 55},
    {'nome': 'Produto4', 'preco': 100},
]

def porcent_value(value, porcent):
    return round(value * porcent)


aumentar_preco_em_dez_porcento = partial(
    porcent_value, 1.10
)

novos_produtos_com_aumento = [
    {**p, 'preco': aumentar_preco_em_dez_porcento(p['preco'])}
    for p in produtos
]

def change_in_product(product):
    return {**product, 'preco': aumentar_preco_em_dez_porcento(product['preco'])}


novos_produtos_com_map = map(
    change_in_product, produtos
)

novos_produtos_com_filtro = filter(
    lambda p: p['preco'] > 10,
    produtos
)

print_list(novos_produtos_com_filtro)
