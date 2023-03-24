"""
a. a união de X com Y (todos os elementos de X e os elementos de Y que não estejam em X)
b. a diferença entre X e Y (todos os elementos de X que não existam em Y)
c. a soma entre X e Y (soma de cada elemento de X com o elemento de mesma posição em Y)
d. produto entre X e Y (multiplicação de cada elemento de X com o elemento de mesma posição em Y)
e. a interseção entre X e Y (apenas os elementos que aparecem nos dois vetores)
"""

from pprint import pprint

vetor_x = [0] * 5
vetor_y = [0] * 5

resultado_a = [0] * 5
resultado_b = [0] * 5
resultado_c = [0] * 5
resultado_d = [0] * 5
resultado_e = [0] * 5

for i in range(5):
    num = int(input('Digite um número para o VETOR X: '))

    while num in vetor_x:
        num = int(input('Digite um número que não foi digitado no vetor X: '))

    vetor_x[i] = num

for i in range(5):
    num = int(input('Digite um número para o VETOR Y: '))

    while num in vetor_y:
        num = int(input('Digite um número que não foi digitado no vetor Y: '))

    vetor_y[i] = num

for i in range(5):
    if vetor_y[i] not in vetor_x:
        resultado_a[i] = vetor_x[i] + vetor_y[i]

    else:
        resultado_a[i] = 'Valor igual'

    if vetor_x[i] not in vetor_y:
        resultado_b[i] = vetor_x[i]

    resultado_c[i] = vetor_x[i] + vetor_y[i]

    resultado_d[i] = vetor_x[i] * vetor_y[i]

    if vetor_x[i] == vetor_y[i]:
        resultado_e[i] = vetor_x[i] + vetor_y[i]

print('-' * 50)

print('Vetor X', vetor_x)
print('Vetor Y', vetor_y)

print('A - A união de X com Y (todos os elementos de X e os elementos de Y '
      'que não estejam em X)', resultado_a)
print('-' * 50)

print('B - A diferença entre X e Y (todos os elementos de X que não '
      'existam em Y)', resultado_b)
print('-' * 50)

print('C - A soma entre X e Y (soma de cada elemento de X com o elemento de '
      'mesma posição em Y)', resultado_c)
print('-' * 50)

print('D - Produto entre X e Y (multiplicação de cada elemento de X com o '
      'elemento de mesma posição em Y)', resultado_d)
print('-' * 50)

print('E - A interseção entre X e Y (apenas os elementos que aparecem nos '
      'dois vetores)', resultado_e)