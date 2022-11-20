cpf = input('Digite seu cpf: ')
lista_cpf = []
for numero in cpf:
    if numero != '.' and numero != '-':
        lista_cpf += numero

lista_a = lista_cpf[:9].copy()
cont = 10
resultado = 0
for i in lista_a:
    print(i)
    resultado += int(i) * cont
    cont -= 1
digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
lista_b = lista_cpf[:10].copy()
cont_2 = 11
resultado = 0
for i in lista_b:
    resultado += cont_2 * int(i)
    cont_2 -= 1
digito_2 = (resultado * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_1, digito_2, lista_b, lista_a, lista_cpf)
digito_1 = str(digito_1)
digito_2 = str(digito_2)
if lista_cpf[9] == digito_1 and lista_cpf[10] == digito_2:
    print('O cpf está correto')
