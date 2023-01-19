from collections import deque
from time import sleep
# livros = list()
# livros.append('Livro 1')
# livros.append('Livro 2')
# livros.append('Livro 3')
# livros.append('Livro 4')
# livros.append('Livro 5') #last in
#
# livro_removido = livros.pop() #first out
# print(livro_removido)
#Com a função deque a gente pode criar uma fila
# FIFO(first in - first out), sem gerar transtornos de armazenamento
# por causa do índece que vai percorre-lá toda

# fila = deque()
# fila.append('Pessoa_na_fila_01')
# fila.append('Pessoa_na_fila_02')
# fila.append('Pessoa_na_fila_03')
# fila.append('Pessoa_na_fila_04')
# fila.append('Pessoa_na_fila_05')
#
# fila.popleft()
# for pessoa in fila:
#     print(pessoa)


# fila_maxima = deque(maxlen=5)
# fila_maxima.append(1)
# fila_maxima.append(2)
# fila_maxima.append(3)
# fila_maxima.append(4)
# fila_maxima.append(5)
#
# print(fila_maxima)
#
# fila_maxima.append(6)
#
# print(fila_maxima)

fila = deque(maxlen=15)

for n in range(100):
    fila.append(n)
    sleep(1)
    print(fila)