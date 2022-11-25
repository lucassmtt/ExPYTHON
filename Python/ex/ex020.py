lista = []
for x in range(1,4):
    for y in range(1,4):
        lista.append((x,y))


list_comprehension = [
    (x,y)
    for x in range(1,4)
    for y in range(1,4)
]

print(lista, 'Lista criando atráves de um "for" normal')
print(list_comprehension, 'List comprehension')


lista_comprehension_dentro_de_outra = [
    [x for y in range(1,4)]
    for x in range(1,4)
]

print('-'* 100)
print(lista_comprehension_dentro_de_outra, 'List comprehension dentro de outra list comprehension')