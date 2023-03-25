"""
Faça um programa que receba dez números e armazene em uma lista.
Em seguida copie todos os números da primeira lista para uma segunda lista,
mas na ordem invertida da primeira lista.
"""

qtd_de_num = int(input('Digite quantos números irão pra lista'))
lista_1 = [0] * qtd_de_num
lista_2 = [0] * qtd_de_num


for i in range(qtd_de_num):
    lista_1[i] = int(input('Digite um número'))

print(lista_1)
cont = qtd_de_num - 1

for i in range(qtd_de_num):
    lista_2[cont] = lista_1[i]
    cont -= 1


print(lista_2)