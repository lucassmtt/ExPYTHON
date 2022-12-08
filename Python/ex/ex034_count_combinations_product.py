from itertools import count, combinations, permutations, product

num = count()

for c in num:
    print(c)
    if c == 2:
        break

def print_iter(iterator):
    print(*list(iterator), sep='\n')


lista_nomes = ['Mylena', 'Lucas', 'Gabriela', 'Medusa']
#print_iter(combinations(lista_nomes, 3))
#print('-'*40)
#print_iter(permutations(lista_nomes, 2))

##PRODUCTS

camisetas = [
    ['branca', 'preta'],
    ['p', 'm', 'g'],
    ['algodão', 'poliéster']
]

print_iter(product(*camisetas))