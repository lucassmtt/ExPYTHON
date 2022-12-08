lista_cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_estado = ['BA', 'SP', 'MG', 'RJ']


def zipper(list1, list2):
    intervalo = min(len(list1), len(list2))
    return [
        (list1[valor], list2[valor]) for valor in range(intervalo)

    ]


####Criando um zipper com função, porém podemos utilizalo com
print(zipper(lista_cidade, lista_estado))


##OUUUUUUUU
from itertools import zip_longest
print(list(zip(lista_cidade, lista_estado)))
print(list(zip_longest(lista_cidade, lista_estado, fillvalue='SEM CIDADE')))