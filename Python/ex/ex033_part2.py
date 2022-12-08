lista_um = [1, 5, 5, 6, 7, 8, 9, 11]
lista_dois = [2, 5, 6, 8, 9, 10]
print(lista_um, 'LISTA UM')
print(lista_dois, 'LISTA DOIS')
def sepador():
    print('-'*30)
sepador()

def joinlist(list_1, list_2):
    new_list_1 = list()
    new_list_2 = list()
    new_list = list()

    for i, v in enumerate(list_1): #pegamos da primeira lista o índice e valor específico que queremos
        new_list_1.append((v))

    for i, v in enumerate(list_2): #pegamos da segunda lista
        new_list_2.append((v))

    intervalo = min(len(list_1), len(list_2)) #adquirimos o intervalo para não dar erro no for

    for valor in range(intervalo):  #vemos o máximo do range, pegamos os índices das duas listas, juntamos e colocamos em outra lista
        new_list.append((new_list_1[valor] + new_list_2[valor]))

    return new_list

nova_lista = joinlist(lista_um, lista_dois)
print('Utilizando uma função que separa e junta listas')
print(nova_lista)
sepador()
##
##OU PODEMOS FAZER PELO MÉTODO DE LISTCOMPREHENSION


lista_nova = [
    x + y for x, y in zip(lista_um, lista_dois)
]
print('Usando o método de list comprehension')
print(lista_nova)


from itertools import zip_longest
lista_nova_com_todos_numeros = [
    x_list1 + x_list2 for x_list1, x_list2 in zip_longest(lista_um, lista_dois, fillvalue=0)
]
sepador()
print('Usando o módulo itertools e importando a função "zip_longest", podemos obter todos os números e assim juntar todos'
      'os números da lista')
print(lista_nova_com_todos_numeros)