from functools import reduce

produtos = [
    {'nome': 'Produto1', 'preco': 10},
    {'nome': 'Produto2', 'preco': 30},
    {'nome': 'Produto3', 'preco': 55},
    {'nome': 'Produto4', 'preco': 100},
]

def reduce_function(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    acumulador += produto['preco']
    return acumulador


##ou usando uma lambda


total = reduce(
    lambda ac, p: p['preco'] + ac,
    produtos,
    0
)

print(total)