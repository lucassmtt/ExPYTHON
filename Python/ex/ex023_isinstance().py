lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1,2),
    {0,1}, {'nome': 'Lucas'},
]

def traco():
    print('-' * 30)


for item in lista:
    if isinstance(item, set):
        print('SET:')
        item.add(5)
        print(item, isinstance(item, set))
        traco()

    elif isinstance(item, str):
        print('STRING')
        print(item.upper())
        traco()

    elif isinstance(item, (int, float)):
        print('INTEIRO OU FLUTUANTE')
        print(item, '* 3 == ', (item * 3).__round__(4))
        traco()

    else:
        print('Outro')
        print(item)