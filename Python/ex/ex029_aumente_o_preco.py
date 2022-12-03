import copy

produtos = [
    {'nome': 'Produto_3', 'preco': 5},
    {'nome': 'Produto_1', 'preco': 4},
    {'nome': 'Produto_4', 'preco': 7.5},
    {'nome': 'Produto_5', 'preco': 9},
    {'nome': 'Produto_2', 'preco': 30}
]

novos_produtos_organizados_por_preco = [
    {**produto, 'preco': produto['preco'] * 1.10}
    for produto in produtos
]

novos_produtos_com_filtro_decrescente = sorted(
    copy.deepcopy(produtos),
    key=lambda produtos : produtos['nome'], reverse= True
)

novos_produtos_com_filtro_preco_crescente = sorted(
    copy.deepcopy(produtos),
    key=lambda preco: preco['preco']
)
print('Produtos originais')
print(*produtos, sep='\n')
print()
print('-'*30)
print('Produtos organizados com filtro de aumento de preço: ')
print()
print(*novos_produtos_organizados_por_preco, sep='\n')
print('-' * 40)
print('Produtos com filtro decrescente: ')
print()
print(*novos_produtos_com_filtro_decrescente, sep='\n')
print('-'* 30)
print('Produtos com filtro de valor: ')
print()
print(*novos_produtos_com_filtro_preco_crescente, sep='\n')